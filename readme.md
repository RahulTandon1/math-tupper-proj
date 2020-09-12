# Grade 12 Math Project on Tupper's Self Referential Formula

For my grade 12 Math project, I partnered up with Harsh Acharya and [Vinayak Singh Bhadoriya](https://www.facebook.com/vinayak.singhbhadoria)
We worked on the Tupper's Self Referential Formula.

We made a presentation to go alongside, which can be found [here](https://docs.google.com/presentation/d/e/2PACX-1vQd8eVCHVvuAJ5n0t9eywa0MN-h0P4JasQk6CcmeBc2vn_Dcp94FWp6QY58AVe-33DeJnUhCbD9ZOC_/pub?start=false&loop=false&delayms=60000)

In case you want the images that we produced, you'll find them in the `/img` folder/directory.

If you're a programmer and want to understand the underlying code, I'll comment the code well sometime. If it's urgent & and I haven't commented the code well, please open an issue in the Github repo.

## What I did

- wrote code in Python with matplotlib
- collaborated with Vinayak to explain how to generate one's own constant, K, to make all kinds of cool plots.

## Inspriation for the Project

- Sidhant Bhavnani's work on his grade 9 project :p: Have a look at it here[https://github.com/scholaronroad/tuppers-self-referential-formula]
- It was used in a level by Code Warriors (DPS VK's Tech Club) in Techathlon (their cryptic hunt).

## Bibliography

I honestly deconstructed, inferred/studied and then partially reconstructed code snippets from @scholaronroad's https://github.com/scholaronroad/tuppers-self-referential-formula.

Other sources of help

- https://stackoverflow.com/questions/8750203/what-is-antialiased-in-matplotlib-collections-and-how-do-you-set-the-paramet
- https://github.com/scholaronroad/tuppers-self-referential-formula/blob/master/tupper-plot.py
- https://keelyhill.github.io/tuppers-formula/
- https://brilliant.org/discussions/thread/write-your-name-with-mathematics/

## Short log

- Glanced through Siddhant's code, watched a bit of Edureka's Matplotlib tutorial. Tried to built stuff out myself.
- Got a repeated error about the "not enough place stuff" (paraphrase). Spent time figuring out what went wrong. The stackoverflow question linked above helped.
- Tried numpy. Error persisted.
- Looked back at Siddhant's code. Understood the catch, and boy oh boy it was a nice catch:
  > He was preserving the original y, simply adding the constant k when evaluating the inequality, then plotting it out.
- Another thing I figured out was the use of the bar plot/chart, which honestly didn't make sense to me initially. I thought we needed something like a scatterplot would go like "here's a bunch of x, y coordinates just plot them, don't connect them as lines." I later figured out that the bar plot, in essence, was being used like a "regular" plot i.e. it just plotted coordinates with each bar acting like a pixel. In the code that you'll find in this repository, a scatterplot is used.

That's the simple short log from how I went from Edureka to Eureka!

## Some brainstorming I did

What I understand
Need to plot an equality
Height of relevant portion is 17 for sure.
Y coordinate to get to is very long integer K.
Width is 106 pixels.

From wikipedia: (x, y) in 0 ≤ x < 106 and k ≤ y < k + 17

## Thank you so much for reading! :)
