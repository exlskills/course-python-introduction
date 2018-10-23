
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
<div data-datacamp-exercise data-lang="python" data-height="500">
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
    6 + 12
  </code>

  <code data-type="sct">
    test_output_contains(&quot;21&quot;, incorrect_msg = &quot;Make sure to add 6 + 12 on a new line. Do not start the line with a #, otherwise your R code is not executed!&quot;)

    success_msg(&quot;Awesome! See how the console shows the result of the R code you submitted? Now that you&#39;re familiar with the interface, let&#39;s get down to R business!&quot;)
  </code>

  <div data-type="hint">
    <p>
    Just add a line of R code that calculates the sum of 6 and 12, just like the example in the sample code!
    </p>
  </div>
</div>
