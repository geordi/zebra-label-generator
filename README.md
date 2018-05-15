# Zebra Label Generator

This is a super simple generator of labels in EPL format that is used in Zebra printers.

## Printer Driver

Follow the [instructions](http://burntweaponsblog.blogspot.cz/2015/09/getting-zebra-printer-working-on-linux.html)
to install Zebra printer driver for Linux.

## Printing

Issus command:

```
lp -d ZPL_II_Printer zebra_example.epl
```

## Generating an EPL file

Run:

```
python3 generate_labels.py
```
The script will go through all files in `data` directory and create one EPL file with all labels.
