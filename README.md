![alt text](https://github.com/Vermillion-Chen/Sportify/blob/main/static/images/Sportify_Logo.png?raw=true)
#### This was a project for the McGill Artificial Intelligence Society Hacks 2021. It is an AI web application that uses computer vision to analyze a user's  workout form, ensuring that good form is kept throughout the duration of a workout. https://devpost.com/software/sportify-5rytap

## Inspiration
Our inspiration comes from the proliferation of people exercising at home, or who are in need of exercising at home because of the recent COVID 19 pandemic. And with restrictions gradually lifting, many are getting back into the habit of exercising, both at home or in a gym. Form is important because it can make the exercise easier, more efficient and give results, whereas bad form can lead to potential injuries and long term physical damage. 

It is difficult to verify your form without your friend or a personal trainer, which not everyone can afford, so there is usefulness in an application that can analyze your form at any moment anywhere. 

## What it does
Sportify is a web application that uses computer vision to track users joints during a workout, and then compares them to a model trained on Olympic athletes to identify if something is wrong with your form. 

## How we built it
Flask, Python, HTML5, CSS for the front-end, Javascript, Pandas, OpenCV, MediaPipe, Scikit-learn for backend

## Challenges we ran into
No well-formatted dataset available online, we had to improvise and hand-pick our own training data. Led to immature model
One of our team members dipped last-minute, so we were down a person.


## Accomplishments that we're proud of
Proud of the front-end and logo, I think the visual design turned out nice. 
Built my first ML pipeline

## What we learned
Learned flask, Javascript, improved web design skills, with things like implementing buttons to attach a file.

## What's next for Sportify
Since Sportify only works on weightlifting, we can improve the model by expanding it to cover more, including body-weight exercises which can be done by anybody at home. This would involve gathering good quality data about good and poor forms for the aforementioned exercises.
