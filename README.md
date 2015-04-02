# CV maker webapp
DevLead:  Alexey Remnev
PM: Alexey Remnev

# Technologies: 
database: mysql/postgre/oracle/mongo/cassandra

language: 
python: django/pyramid

ruby: rails

node: express

php: symphony/zend/(cake/drupal)

perl: Catalyst

UI: bootstrap/jquery/backbone/angular/sass/less

# Introduction
Create web application for creation and sharing CV. This document describes general idea, which can be extended easily in sense of scope.
# Functional requirements
Features

- Registration through linkedIn or google+ api (OAuth)
- Creation and saving CV with required and custom sections.
- html5 markup

List of pages

- main page
- Profile page with CV’s list
- CV edit page (append, remove section)
- CV detail page (export pdf, .doc, .html)

# Technical requirements
Server side

- Implementation language: python/ruby/node/php
- CV storage: mysql/oracle/mongo/cassandra

Browser side

Design
- Use Bootstrap as quick design/styling solution.
- jQuery for interactive elements/
- (advanced interactions) Angular or Backbone.
