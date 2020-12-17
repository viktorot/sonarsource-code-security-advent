# Day 1 - Django

### Challenge

You can find the original challenge [here](https://twitter.com/SonarSource/status/1333803048599121921).

### Vulnrability

This code is vulrable to and [open redirect](https://portswigger.net/kb/issues/00500100_open-redirection-reflected) vulnrability.

The vulnrable code allows an attacker to specify the value of a parameter that is later used to redirect the user to a URL set by the attacker.

The vunrable code is found in the `register.py` file. The `dispatch` function processes incomming `GET` requests. It checks to see wether the `next` query parameter is set and redirects the user there. Otherwise it fallsback to the default which is `/`.

### Building and running the app

In order to run the app you will need `docker` and `docker-compose` installed. Once you have everything setup, just run:

1. `docker-compose  build`
2. `docker-compose up`

To test if everything is working correctly, navigate to `localhost:8080` in your browser. If you see a `Hello, world!` message, you know everything is working correctly.

### Exploitation

Exploiting the vulnrability is straitforward here. By simply navigation to `localhost:8080/register?next=[external_url]` and supplying the `next` query parameter, we make the system redirect the user to wherever we like.