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

## A quantitative but non-inductive approach to cyber-security risk assessment

Several standards mandate a secure-by-design
approach in which cybersecurity shall be considered at the very early
stages of the design process. For example, the DO-326A – "Airworthiness
Security Process Specification" requires a cybersecurity risk assessment of
the design and "are the only Acceptable Means of Compliance (AMC) by
FAA & EASA for aviation cybersecurity airworthiness certification, as of
2019" as pointed out by SAE. Standards do not describe in detail how to
perform a cybersecurity risk assessment and only vaguely define the overall objective, which can be summarized as to provide an understanding of
the potential cybersecurity risks.
In this thesis, the student will work on the correlation between the hypothesis that errors can be used as a measure of the cybersecirity risk and
focus on one of the following (or whatever great ideas you have):

* choose a CPS type that she likes (automotive? aerospace?) and review a relevant cybersecurity (engineering) standard.
* review current research approaches to the cybersecurity risk assessment (e.g. CORAS).

Want more? We already reviewed many standards and approaches and we
created our own risk assessment prototype, but we are still lacking many
fundamental features such as:

* a proper formalization of asset diagrams (what the business guys
want to protect) and their correlation to the engineering of systems
(what the tech guys have built).

* Proper calculation of a risk matrix (likelihood and impact) – do you
have an educated guess on the likelihood of an error and on the
correlations to cybersecurity attacks?
