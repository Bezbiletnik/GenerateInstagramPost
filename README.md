# Real Estate Instagram Post Generator

## Overview
*This Python script generates Instagram posts for real estate listings using OpenAI's GPT-3.5-turbo model. 
The script reads random entries from a housing dataset, formats the data, and creates compelling Instagram posts for each listing.*
___

## Setup
+ ```python -m pip install -r requirements.txt```
___

## Features
Parallelism was used to increase the speed of the ChatGPT answer. 
By this approach, the time taken for processing 20 entries decreased by 10 times from ~10 minutes to ~50sec instead.

## Libraries

The program was written in **Python**.
+ [OpenAI](https://platform.openai.com/docs/overview)
+ [Pandas](https://pandas.pydata.org/)

___

## Example Response

price=6230000<br>
area=5500<br>
bedrooms=3<br>
bathrooms=1<br>
stories=3<br>
mainroad=yes<br>
guestroom=no<br>
basement=no<br>
hotwaterheating=no<br>
airconditioning=no<br>
parking=1<br>
prefarea=yes<br>
furnishingstatus=unfurnished<br>
// all parameters used to generate this sample<br>
🏡 Just Listed! This gorgeous 3-bedroom home with 1 bathroom is now available for only $6,230,000! Don't miss out on this amazing deal! 🙌

📐 With a spacious area of 5,500 sqft, this home offers plenty of room for your family and guests to relax and enjoy. 🌳🌞

🛏️ Featuring 3 cozy bedrooms, this home provides ample space for everyone to have their own privacy while enjoying quality time together. 💤✨

🚻 The bathroom is well-maintained and ensures your daily routines are convenient and comfortable. 🚿💦

🏢 This 3-story home offers a versatile layout, perfect for families looking for extra space and separation. 📚🎮 

🛣️Situated on the main road, you'll have easy access to nearby amenities, transportation, and entertainment options. 🛒🚌

🏠 The property also includes a parking space, ensuring convenience and peace of mind for you and your family. 🚗🅿️

🏖️ Located in a preferred area, you'll enjoy a peaceful and serene neighborhood, perfect for long walks and leisurely evenings. 🌳🌸

❄️💦 Other features include hot water heating and air conditioning, providing comfort in any weather. 

💼💼 Whether you're a family looking for a spacious home or an investor seeking an excellent property, this listing is a must-see!

📲 Contact us today to book a viewing! Don't wait, as this incredible opportunity won't last long! 📞💼

#JustListed #DreamHome #FamilyFriendly #RealEstate #InvestmentOpportunity #HomeSweetHome
