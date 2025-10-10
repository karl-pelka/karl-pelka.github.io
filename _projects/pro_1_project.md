---
layout: page
title: AI music news
description: Fully automated song generation and social media upload
img: assets/img/codeblog/AImusic.webp
importance: 1
category: programming
related_publications: false
---

I started working on an AI project for automated music generation and release on YouTube. The code has a few simple functionalities chained into each other. The first bit grabs a news of the day and sends it with a prompt to generate a corresponding lyrics to [Gemini AI](https://ai.google.dev/) along with a prompts on which music genre and what scenery fit the mood of the text. The lyrics and the prompt are then sent to [Mureka AI](https://www.mureka.ai/de/create) to generate the song and to [Black Forest Labs](https://www.bfl.ai) FLUX.1-schnell model to generate a matching thumbnail. The code then downloads both source files (music and thumbnail) and merges them into a video before it is uploaded automatically through the YouTube Data API v3 to YouTube. The result can be seen here.

<div style="text-align: center">
<iframe
  src="https://www.youtube-nocookie.com/embed?listType=playlist&list=UUkaH3bF_jalv2ioSh2hQ6mg"
  width="600"
  height="340"
  allowfullscreen>
</iframe>
</div>

The code will be uploaded to GitHub soon and I have a few updated features on my mind.

