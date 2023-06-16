# Bloc 5 - Industrialisation d'un algorithme d'apprentissage automatique et automatisation des processus de décision - Getaround analysis

[Presentation video](https://share.vidyard.com/watch/1ke5pSftHJgm8rb7yBQXwF?)

Dashboard: https://cnmgetaroundanalysis.herokuapp.com

API: https://cnmgetaroundprediction.herokuapp.com/docs

### Introduction

Getaround is an American online car sharing service founded in 2009 in San Francisco and launched to the public in 2011. It is now the European leader for car sharing, connecting drivers who need a car to car owners.

### Problematic

- 1 - Getaround has experienced problems with unsatisfied users due to late car returns from the previous driver. The company would like to optimize the delay between two rentals.

- 2 - Getaround currently works on pricing optimization. The company would like to suggest an optimum price to car owners depending on the characteristics of their car.

### Scope

To optimize the delay between two rentals, the product manager of Getaround needs some insights to define the right trade off that would solve the late check-outs issue without impacting the car owners' revenues. For this purpose, Getaround provided a dataset containing information on car shares, which included information on potential cancelation of the shares, check-out time for ended shares, and information on the previous share when applicable.

To optimize the price of rentals for car owners, Getaround would like to develop an API that would predict an optimum price based on cars' characteristics. For this purpose, the data science team provided a dataset containing information about cars, and the corresponding prices that are currently applied.

### Aims and objectives

**Aim 1: Build a dashboard that would help the product manager make a decision about late check-outs.**

Objectives:
- 1 - Evaluate the proportion of late check-outs and their impact on the next driver.
- 2 - Evaluate the benefits of the new feature for car drivers and car owners.
- 3 - Evaluate the global impact of the new feature on car rentals and cancelations.
- 4 - Evaluate the proportion of problematic cases solved by the new feature and the proportion of rentals that would be affected.

**Aim 2: Build an API that would predict an optimum rental price depending on cars' features.**

Objectives:
- 1 - Develop a machine learning model that would predict an optimum rental price.
- 2 - Develop an API for price prediction.
- 3 - Test the API functionality.
