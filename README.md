# KiSelect
A tool for KiCad enabling different methods of search / selection.

https://github.com/HiGregSmith/KiSelect

Unchangable default (at the moment) is case insensitive, partial word.

It works with recent Nightly versions of KiCad.

Note that a Nightly is not guaranteed to produce files that can be opened with the stable release. It does not even guarantee that the nightly of yesterday can open a file produced by the nightly of today. (In most cases it works but know what you get into if you decide to use nightlies.)

    INSTALLATION

    KiSelect is a ActionPlugin and is installed similar to other Action Plugins.
    Place the kiselect.py file in 
    C:\Program Files\KiCad\share\kicad\scripting\plugins
    Or the equivalent in MacOS or Linux
    (there may be a user-level directory for such files, but I am not aware of it at the moment.)
    Within KiCad pcbnew, select the Tools > External Plugins > Refresh Plugins

    Selection dialog box is shown when the "Select..." menu item is selected.
