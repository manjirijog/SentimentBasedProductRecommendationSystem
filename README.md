# SentimentBasedProductRecommendationSystem

This project is to design a Sentiment-Based Product Recommendation System for an e-commerce company named 'Ebuss'. Ebuss has captured a huge market share in many fields, and it sells the products in various categories such as household essentials, books, personal care products, medicines, cosmetic items, beauty products, electrical appliances, kitchen and dining products and health care products.

With the advancement in technology, it is imperative for Ebuss to grow quickly in the e-commerce market to become a major leader in the market because it has to compete with the likes of Amazon, Flipkart, etc., which are already market leaders.

As a senior ML Engineer, you are asked to build a model that will improve the recommendations given to the users given their past reviews and ratings.

In order to do this, you planned to build a sentiment-based product recommendation system, which includes the following tasks.

**1. Data sourcing and sentiment analysis** -  Analyse product reviews after some text preprocessing steps and build an ML model to get the sentiments corresponding to the users' reviews and ratings for multiple products.

**2. Building a recommendation system** - Use the following types of recommendation systems.

  1. User-based recommendation system
  2. Item-based recommendation system
  
Once the best-suited recommendation system is obtained, the next task is to recommend 20 products that a user is most likely to purchase based on the ratings.

**3. Improving the recommendations using the sentiment analysis model** - Further, link this recommendation system with the sentiment analysis model that was built earlier (recall that we asked you to select one ML model out of the four options). Once you recommend 20 products to a particular user using the recommendation engine, you need to filter out the 5 best products based on the sentiments of the 20 recommended product reviews.

**4. Deploying the end-to-end project with a user interface** - Once the ML model and the best-suited recommendation system are finalized, the project is deployed end-to-end using Flask framework, which is majorly used to create web applications to deploy machine learning models.

To make the web application public, Heroku is used, which works as the platform as a service (PaaS) that helps developers build, run and operate applications entirely on the cloud.