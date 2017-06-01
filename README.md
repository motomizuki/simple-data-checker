# Tarsier

Tarsier is a simple data check framework that helps inspired by Embulk.
Tarsier consists 3 plugins
 - input plugin : loaded data from data store. (csv, nosqldb, sqldb, api etc)
 - checker plugin : checked loaded data. (upper limit, lower limit, detected luck of data etc)
 - output plugin : execute some action when checker rule matched.  (mail, slack, file, etc)

Tarsier supports plugins to add functions.
