# AddCaps

Glyphs Filter for automatically adding cap components to your outline. This makes most sense for script typefaces in order to facilitate overlaps at where the letter shapes are supposed to connect.

### Instructions

Add a *Filter* custom parameter like this to your instance:

```
AddCaps; cap:_cap.xxx; 100,200; width-20,300
```

This will add the cap component `_cap.xxx` to the nodes at the semicolon-separated list of coordinates. In this case at the node at x=100, y=200, and at the node at x=20 units left from the RSB, y=300.

The node coordinate has a tolerance of 10 units.

You can specify specific glyphs by adding `exclude:` or `include:` directives, followed by a comma-separated list of glyph names, e.g.:

```
AddCaps; cap:_cap.xxx; 100,200; width-20,300; include: a,b,c,d,e,f,g
```

### Requirements

The plugin needs Glyphs 2.6.1 or higher, running on OS X 10.9 or later. I can only test it in current OS versions, and I assume it will not work in older versions.

### License

Copyright 2019 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Jan Gerner (@yanone) and Georg Seifert (@schriftgestalt).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
