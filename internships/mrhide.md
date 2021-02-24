## Vaguely defined objective

We want to have a system/software that:
1. during a live meeting, captures the video from the webcam,
2. modifies the video so that the image of the speaker is hidden (e.g. completely black), and
3. generates a token for each participant such that, if shared (e.g. via email), the image of the speaker becomes not-hidden

#### Requirements (draft)

- *Authentication*: only those who are trusted should see the speaker in the video
- *Confidentiality*: the image of the speaker should not be visible/understood while in transit but only at rest
- *Integrity*: the image of the speaker should be preserved during the transferring (in transit)

#### Potentially useful links

* [Linux Fake Background](https://github.com/fangfufu/Linux-Fake-Background-Webcam)
