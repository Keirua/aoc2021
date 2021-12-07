
My python CLI to make repetitive tasks simpler:
 - downloading an input in a consistent way
 - creating a python file with a few `imports`, and the input file already read
 - opening AoC’s puzzle page

# Configuration

All you have to do is set your cookie inside a `settings.ini` file, by following the syntax in `settings.example`

# Usage

 - `cli bootstrap` will download today’s input, and create a template that opens the input. The template uses some code from aoc.py, but you may not need that.
 - `cli open` opens todays puzzle page, `cli open -d 4 -y 2015` opens a specifi puzze
 - `cli run` runs todays code, or you can run a specific day with `-d` and/or `-y`
