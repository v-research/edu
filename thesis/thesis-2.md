## Overview

We have a question: what is cybersecurity? Or, even better, what
is a cyber-secure system? People believe that cybersecurity can be defined as
a property (e.g., confidentiality) but, can we say that a system in which that
property holds is actually secure? Obviously not, just publish any
confidentiality scheme and wait 5 minutes :) Well... maybe cybersecurity is a
set of
properties? Again, show me that system in which those properties hold and
I bet I'll find an insecurity somewhere. So, if a cybersecure system is the one
without cybersecurity attacks, is there a set of properties that makes that
system secure? No! That's the point! Those who wear a black hat don't care
about how we define security. Nor the entire universe. A scientific hypothesis
on what a cybersecure system is must predict the security and insecurities of
that system so we can empirically test the predictions (i.e. trying to hack our
way into the supposedly secure system). After, and only after, one can become
the "momentary [cybersecurity] master of a fraction of a dot" or desperately
hope in a "better luck next time".
It is evident that an attack (an authentication bypass) is made possible by
a vulnerability (a sql-injection) which, in turn, is made possible by an error
somewhere in the design or implementation of a system (or procedure, e.g., an
authentication system).

*A*: So, what if we had a system (or a piece of code) that is error-free?
*B*: It's impossible!
*A*: Ok, but what if? Wouldn't we have a secure system?
*B*: Well, ok... you theorist! Is having an impossible secure system of any use?
*A*: Maybe? While it's true that a human being cannot fly, it's also true that
there are interesting approximations such as airplanes or the ESS. So, let's
stop with the chattering and start building a trivial ("thanks" Rice... )
system secure by trying predicting all its errors!
*B*: Wait... what's an error?
Sorry, "there's no royal road to science" and while it may be easy to grasp
the path we're following, there's a bit of math that you've got to digest before.
If you are interested in helping us "carrying the [cybersecurity] stone", we'll
share with you our paper on a theory of error (and we'd be happy to discuss it
with you) and collaborate to one of the following thesis.

# I'm an engineer -- A formal approach to the engineering of security protocols and cyber-physical systems

The bulk of the question is, obviously, what you want to do with your system. Can you break it down to a
number of functions so that we can try to predict errors at a microscopic
scale? This engineering is far from trivial, and you'll get to know how
loosely defined are the specifications of systems, but it is always rewarding living those 5 seconds where the whole engineering seems just perfect,
working... and then inevitable falling apart, down to "how could I believe
that it was working!"
In this thesis, the student will review current approaches and languages
for the engineering of systems and security protocol. He will then focus
on proposing all of the following:
* her engineering view on systems and protocols, and
* a prototype engineered system or protocol so that an estimation of the cybersecurity risk is provided as a correlation between known attacks to engineering choices or errors.
