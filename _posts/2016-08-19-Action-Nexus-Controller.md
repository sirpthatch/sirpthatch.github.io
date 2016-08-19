---
layout: post
date: 2016-08-19
title: Action Nexus Controller
tags: [akka, code]
---

I have been using a simple design pattern for my project as of late, and found that is enables me to jump in and out of development very easily.  My usual side project m/o is to work on it off and on when I have time.  Thus, large, complicated abstractions and interlocking components means I spend more time getting myself repositioned within a project than I do actually contributing code.  Sub optimal!

In truth, what follows is not something that I would probably use much in a professional context - usually there is another way - however my side project development is far from a professional project.

### Enter: Action Nexus Controller

Here is the core class:

```scala
case class ActionNexusActor(children:Seq[ActorRef]) extends Actor with LazyLogging{

  var pendingActions:Seq[Event] = Seq.empty[Event]
  var pendingQuestions:Seq[QuestionRecord] = Seq.empty[QuestionRecord]
  var outstandingQuestions:Seq[QuestionRecord] = Seq.empty[QuestionRecord]

  override def receive: Receive = {

    case IamYourNexus =>
      children.foreach(_ ! IamYourNexus)

    case req:Event =>
      pendingActions = pendingActions :+ req

    case Retrospective =>
      pendingActions = pendingActions :+ Event(Retrospective)

    case Heartbeat(timeStamp) => {
      val beat = Heartbeat(DateTime.now())

      (pendingActions ++ pendingQuestions.map(_.question)).foreach {
        action =>
          logger.debug(s"Broadcasting action: $action")
          children.foreach{ _ ! action }
      }
      outstandingQuestions = outstandingQuestions ++ pendingQuestions

      children.foreach( _ ! beat )

      pendingActions = Seq.empty
      pendingQuestions = Seq.empty
      outstandingQuestions = outstandingQuestions
        .filterNot(
          question =>
            new time.Duration(question.question.timeStamp, timeStamp).getStandardSeconds > question.question.timeout.toSeconds)
    }

    case quest:Question =>
      logger.debug(s"Logging question: ${quest} from ${sender().path}")
      pendingQuestions = pendingQuestions :+ QuestionRecord(sender().path, quest)

    case questResponse:QuestionAnswer => {
      logger.debug(s"Received questions response: $questResponse")
      outstandingQuestions
        .filter(r => r.question.id == questResponse.questionId)
        .foreach {
          case QuestionRecord(sender, _) =>
            logger.debug(s"Routing response to all children")
            children.foreach( _ ! questResponse )
        }
    }
  }
}
```

What do we have here?  To break it down - this is a broadcasting controller, which repeats messages to all of its children.  It is using Akka Actors - a pattern described well [here](http://doc.akka.io/docs/akka/current/scala/actors.html).  Basically, actors are encapsulations of state and behavior that communicate (most of the time asynchronously) by passing messages back and forth.   

Most of the logic of my projects lives within Actors that are children of an ActionNexusController - doing so allows me to build a component in isolation that then seamlessly integrates with other components in the overall system.  For instance - in my quant life project, I have a system which is responsible for sending out surveys, and separate systems which record responses, build predictive models based on responses, figure out if I am ignoring the surveys, etc.  The only thing that these sub systems have to know about is the type of messages sent by others - they can filter for those messages and do whatever they need to do.

So some key strengths of this, as I see it:

* Components are decoupled - their messages get pooled together and redistributed, so routing is taken care of
* Things are intervalized - this is a convenience, makes it easy to see the state of computation and make some more formalized assertions about the sytem as a whole
* Networkable - in more tricky setups, I have ActionNexusControllers that are children of other ActionNexusControllers.  This enables non-trivial messaging systems to emerge, where certain information is shared locally and other information is broadly distributed
* Debugging - since all the messages flow through the ActionNexusController, it is easy to intercept and see how they are being handled

Some obvious weaknesses:

* Not good for high throughput - duplicates messages and sends them around to children, regardless of whether they want to handle them or not
* Not performant - the intervalization is purposefully designed to slow things down

Like I said, this is probably not something I would use professionally, but it is a nice accelerant for my personal projects.
