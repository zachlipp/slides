# Slides

A collection of my personal `reveal.js` slides generated with `reveal-md`. This is just getting started now, so expect changes in the future.

## Running

Presentations can be run with the following command (I know it's gross; I'm working on it):

```
docker run \
  --rm \
  --name slides \
  -p 1948:1948 \
  -v "$(pwd)":/home \
  --entrypoint reveal-md \
  <name-of-image> \
  --template master.html \
  --css footer.css  \
  <path-to-slides>
```

