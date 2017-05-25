# Simple-data-checker

Simple-data-checker is a simple data check framework that helps inspired by Embulk.
Simple-data-checker consists 3 plugins
 - input plugin : loaded data from data store. (csv, nosqldb, sqldb, api etc)
 - checker plugin : checked loaded data. (upper limit, lower limit, detected luck of data etc)
 - output plugin : execute some action when checker rule matched.  (mail, slack, file, etc)

Simple-data-checker supports plugins to add functions.
