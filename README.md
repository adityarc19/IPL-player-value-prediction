# IPL Player Value Prediction [web app](https://ipl-player-value-pred-app.herokuapp.com/)

![money gif][logo]

[logo]: https://github.com/adityarc19/IPL-player-value-prediction/blob/main/images/tenor.gif

#### * In this web app, prediction of 'value' is made on the basis of data of all past IPL seasons (2008 to 2020).
The value of each player is estimated by calculating how much above average that player contributed as a batsman or a bowler. Both the batting and bowling scores are combined into a single score called Runs Above Average, or RAA. An RAA score of 0 implies an average performance. A positive RAA means that the player was above average, and conversely a player with negative RAA means his performance was below average. 
The value of a player is the overall average salary, plus a value that is proportional to the total RAA score of the player. Basically, the player valuation methodology re-distributes the total spend of the teams to the players based on their performance.

[Source](http://www.cricmetric.com/blog/2015/05/how-much-was-each-player-actually-worth-in-ipl-2015/)

#### * I have used 'Extreme Gradient Boosting' as a regression model for this prediction problem. 


Check out [scikit-learn website](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html) for more on OMP model usage. 

#### Some results are:
 1. **Metrics**
 
![metrics][a]

[a]: https://github.com/adityarc19/IPL-player-value-prediction/blob/main/images/metrics.jpeg?raw=true

2. **Hyperparams used**

![hyperparams][b]

[b]: https://github.com/adityarc19/IPL-player-value-prediction/blob/main/images/hyperparams.png?raw=true

3. **Residual plot**

![res_plot][c]

[c]: https://github.com/adityarc19/IPL-player-value-prediction/blob/main/images/residual%20plot.png?raw=true

4. **Prediction error plot**

![pe_plot][d]

[d]: https://github.com/adityarc19/IPL-player-value-prediction/blob/main/images/prediction%20error%20plot.png?raw=true

5. **Learning curve plot**

![lc_plot][e]

[e]: https://github.com/adityarc19/IPL-player-value-prediction/blob/main/images/learning%20curve.png?raw=true

6. **Validation curve plot**

![vc_plot][f]

[f]: https://github.com/adityarc19/IPL-player-value-prediction/blob/main/images/validation%20curve.png?raw=true

