# ⛔️ DEPRECATED

A collection of my personal `reveal.js` slides generated with `reveal-md`.

I've deprecated this project. `reveal-hugo` suits my needs much better, see [my site](https://github.com/zachlipp/lippingoff) for details.

## Project goals

There's a pretty simple goal hiding underneath this ugly implementation: I want to generate `reveal.js` slides from markdowns and I am willing to go to too long of lengths to avoid messing around with node.

## Running

Generate presentations using make commands:

- `make live-render` runs a `reveal-md` server in Docker. Use this while editing presentations.
- `make static-render` generates the slide show as a static website. Use this to finish a presentation.

Pass the presentation you want to render with the command line argument (okay, *technically* environment variable) `PRESENTATION_NUMBER`, e.g. `make live-render PRSENTATION_NUMBER=0`.
