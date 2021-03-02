===========
Employee Id By Nationality
===========

This module supports sequence of employee ID which will be generated
automatically from the sequence predefined.

Nevertheless, if you need a difference ID in particular cases
you can pass a custom value for `identification_id`: if you do it
no automatic generation happens.

**Table of contents**

.. contents::
   :local:

Installation
============

To install this module, you need to:

* clone the branch 12.0 of the repository https://github.com/ihebltaief/share
* add the path to this repository in your configuration (addons-path)
* update the module list
* search for "Employee Id By Nationality" in your addons
* install the module

Configuration
=============

If you want to modify the format of the sequence, go to
Settings -> Technical -> Sequences & Identifiers -> Sequences
and search for the "Employee Identifier By Nationality" sequence, where you modify
numbering formats...


Usage
=====

When you will create or import a new employee, the field reference will be
assigned automatically with the next number of the predefined sequence and with nationality code prefix.

Known issues / Roadmap
======================

* When installing the module, the ID of existing employees is not generated automatically

Credits
=======

Authors
~~~~~~~

* Iheb Ltaief

Contributors
~~~~~~~~~~~~

* Iheb Ltaief <ihebltaief@gmail.com>

Maintainers
~~~~~~~~~~~

This module is maintained by Iheb Ltaief.
