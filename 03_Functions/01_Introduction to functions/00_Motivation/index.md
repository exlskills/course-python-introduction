
### Motivations
- Creates cleaner code
- Reusable in the future
- Get rid of unnecessary messy lines of code

You can call a function in a python script and reuse it multiple times.  This means that if you have the same code repeating, it makes more sense to write a function rather than repeat the code.

### Parts of a function:

1. Declaration with function name and **arguments** that are passed to the function.
2. Doc String which describes the purpose of the function.
3. Code that executes inside the function.
4. Return statement that sends back information.

In the next slide, we explore what each of the pieces looks like!


<div class="exercise">
    <div class="title">
      <h2>This is an python exercise with a plot</h2>
    </div>

    <div data-datacamp-exercise data-lang="python" data-height="auto">
      <code data-type="pre-exercise-code"></code>
      <code data-type="sample-code">
        import numpy as np
        import matplotlib.pyplot as plt

        x = np.arange(0, 5, 0.1);
        y = np.sin(x)
        plt.plot(x, y)
        plt.show()
      </code>
      <code data-type="solution"></code>
      <code data-type="sct"></code>
      <div data-type="hint">Just press 'Run'.</div>
    </div>
  </div>
  <div class="exercise">
    <div class="title">
      <h2>How it works</h2>
    </div>
    <div data-datacamp-exercise data-lang="r" data-height="500">
      <code data-type="pre-exercise-code"># no pec</code>
      <code data-type="sample-code">
        # Calculate 3 + 4
        3 + 4

        # Calculate 6 + 12
      </code>
      <code data-type="solution">
        # Calculate 3 + 4
        3 + 4

        # Calculate 6 + 12
        6 + 12</code>
      <code data-type="sct">
        test_output_contains(&quot;18&quot;, incorrect_msg = &quot;Make sure to add `6 + 12`
        on
        a new line. Do not start the line with a `#`, otherwise your R code is not executed!&quot;)
        success_msg(&quot;Awesome! See how the console shows the result of the R code you
        submitted? Now that you&#39;re familiar with the interface, let&#39;s get down to R
        business!&quot;)
      </code>
      <div data-type="hint">
        <p>Just add a line of R code that calculates the sum of 6 and 12, just like the
          example
          in the sample code!</p>
      </div>
    </div>
  </div>
