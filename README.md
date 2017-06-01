# Tarsier

Tarsier is a simple data check framework that helps inspired by Embulk.
Tarsier consists 3 plugins
 - input plugin : loaded data from data store. (csv, nosqldb, sqldb, api etc)
 - checker plugin : checked loaded data. (upper limit, lower limit, detected luck of data etc)
 - output plugin : execute some action when checker rule matched.  (mail, slack, file, etc)

### Install

```
pip install tarsier
```

### Run checker

```bash
tarsier run config.yml
```

### Plugins
#### Install
```
pip install tarsier-input-mongodb
```

#### Preinstall plugins
|category|type|name|description|
|:---:|:---:|:---:|:---:|
|input|csv|tarsier-input-csv|csv input plugin|
|checker|always|tarsier-checker-always|checker plugin witch always returns true|
|checker|threshold|tarsier-checker-threshold|checker plugin that checks upper and lower|
|output|std|tarsier-checker-threshold|output to stdout|

### Config
The tarsier setting is defined with yaml.

+ in: define what type of input plugin to use.
+ checker: define what type of checker plugin to use.
+ out: define what type of output plugin to use.

When csv (device.csv) is input and there is a device whose cost is 300 or less When standard output is performed The following config.yml is obtained

[device.csv]
```csv
device_id,device_name,cost
1,hoge,1000
2,fuga,10000
2,fugo,200
```

[config.yml]
```yml
in:
  type: csv # input plugin type
  path: device.csv # plugin config

checker:
  type: threshold # checker plugin type
  field: cost # plugin config
  upper: 300 # plugin config

out:
  type: std # output plugin type
```

