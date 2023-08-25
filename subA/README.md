subA Amazing Optimization Method
======================================
We are pretending that this is an optimization tool such as POUNDERS with a MATLAB and a Python implementation.  Please see [POUNDERS](https://github.com/POptUS/IBCDFO/blob/main/pounders) for an example of tool implementation.

We imagine that subA shares some commonality with subB so that it is sensible
for both to be packaged together in
[mytemplate_pypkg](https://github.com/jared321/mytemplate/tree/main/mytemplate_pypkg/src/mytemplate).
However, since subA and subB are separate tools, they are located in the repo as
separate folders for independent development.

Testing
=======
Since this tool is included in [mytemplate_pypkg](https://github.com/jared321/mytemplate/tree/main/mytemplate_pypkg/src/mytemplate) via symlink, it should be tested through that package.
