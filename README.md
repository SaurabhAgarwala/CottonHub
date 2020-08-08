# CottonHUb
Team CodeBreakers novel solution for problem statement AR256 given by the Ministry of Textile in SIH 2020

## Features

CottonHub is an e-commerce portal that streamlines and simplifies the purchasing as well as sales of cotton.  It provides a platform for cotton farmers to upload their information and selling price so that customers can easily find suitable cotton in a market near them.

In addition to its e-commerce facilities, CottonHub features an artificial Intelligence based solution which calculates the future market trend of cotton sales on the basis of past years data and predicts the price of cotton on a market and variety basis. Farmers may use this as a guideline to price their cotton. 

Cotton is a commodity, which is perhaps the most volatile among all the agricultural commodities traded. Due to high voiatility in cotton prices, it is very difficult for farmers to manually guess the future market trend and accordingly strategize their sales so as to compete in the market and increase the volume of the corporation for sustainable growth. Thus, our artificial Intelligence based solution is a critical tool for farmers to bolster their income!

## Running the code: Web App
- Navigat to AR256_CodeBreakers/web_app/CottonHub
- Setup a virtual env
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

## Running the code: Mobile App
### Getting Started 

- `Clone project`
- Execute `flutter pub get` to fetch packages
- Execute `flutter run` to start the app (Emulator should be running or a device should be connected.)

### Emulator
To create a device <br>
`flutter emulators --create [--name xyz]`

To start emulator <br>
`flutter emulators --launch <id>`

To list all devices <br>
`flutter emulators`

