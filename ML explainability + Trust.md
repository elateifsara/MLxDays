# Explainability + Trust

Please visit [this website](https://pair.withgoogle.com/chapter/explainability-trust/) for more in depth information.

The following are notes taken from the Explainability + Trust chapter in the People AI Guidebook (PAIR) from Google.

This chapter demonstrates the importance of explaining your predictions output to your users to gain their trust and keep them aware of the shortcomings of your model. It also explains best practices on how to display the performance of your model and explain its shortcomings.

We have 3 key considerations to remember to explain AI systems:

    1- **Help users calibrate their trust:** The user should know when to trust the system's predictions and when to apply their own judgement.
    2- **Optimize for understanding:** In some cases it's difficult to explain to users the output of the algorithm.
    3- **Manage influence on user decisions:**  If, when, and how the system calculates and shows confidence levels can be critical in informing the user’s decision making and calibrating their trust.
    
## Help users calibrate their trust
Users shouldn’t implicitly trust your AI system in all circumstances, but rather calibrate their trust correctly.

### Articulate data sources
**Key concept**

Whenever possible, the AI system should explain the following aspects about data use:

    - **Scope**. Show an overview of the data being collected about an individual user, and which aspects of their data are being used for what purpose.
    - **Reach**. Explain whether the system is personalized to one user or device, or if it is using aggregated data across all users.
    - **Removal**. Tell users whether they can remove or reset some of the data being used.
    
### Tie explanations to user actions
People learn faster when they can see a response to their actions right away, because then it’s easier to identify cause and effect. This means the perfect time to show explanations is in response to a user’s action. If the user takes an action and the AI system doesn’t respond, or responds in an unexpected way, an explanation can go a long way in building or recovering a user’s trust. On the other hand, when the system is working well, responding to users’ actions is a great time to tell the user what they can do to help the system continue to be reliable.

### Account for situational stakes
**Key concept**

As a team, brainstorm what kinds of interactions, results, and corresponding explanations would decrease, maintain, or inflate trust in your AI system. These should fall somewhere along a trust spectrum of “No trust” to “Too much trust”.

Here are some examples from our running app:

    - A user who has never run more than 3 miles at a time receives a recommendation for a marathon training series.
    - A user takes the training recommendation to their personal trainer and their trainer agrees with the app’s suggestion.
    - A user follows the app’s suggestion for a recovery run, but it’s too difficult for them to complete.
    
## Optimize for understanding
### Explain what’s important
### Describe the system or explain the output
### Data sources
Describe influential feature(s) for the user in a simple sentence or illustration.
### Model confidence displays
Rather than stating why or how the AI came to a certain decision, model confidence displays explain how certain the AI is in its prediction, and the alternatives it considered. 
**Examples:**
    - N-best most-likely classifications
    - Numeric confidence level
### Example-based explanations
This approach gives users examples from the model’s training set that are relevant to the decision being made. 
### Explanation via interaction
Another way to explain the AI and help users build mental models is by letting users experiment with the AI on-the-fly, as a way of asking “what if?”. People will often test why an algorithm behaves the way it does and find the system’s limits.
**Note** special cases of absent or comprehensive explanation:
    - Consider using partial explanations and weigh the impact on user trust.
    - If you are required to give a complete explanation of your model, there are additional considerations for protecting private data that may have been used to train the model.
    
**Key concept**
Think about how an explanation for each critical interaction could decrease, maintain, or increase trust. Then, decide which situations need explanations, and what kind. The best explanation is likely a partial one.

There are lots of options for providing a partial explanation, which intentionally leave out parts of the system’s function that are unknown, too complex to explain, or simply not useful. Partial explanations can be:

    - **General system.** Explaining how the AI system works in general terms
    - **Specific output.** Explaining why the AI provided a particular output at a particular time
    
## Manage influence on user decisions
Displaying model confidence can sometimes help users calibrate their trust and make better decisions, but it’s not always actionable. In this section, we’ll discuss when and how to show the confidence levels behind a model’s predictions.

### Determine if you should show confidence
Be sure to set aside lots of time to test if showing model confidence is beneficial for your users and your product or feature. You might choose not to indicate model confidence if:

    - **The confidence level isn’t impactful**. If it doesn’t make an impact on user decision making, consider not showing it. Counterintuitively, showing more granular confidence can be confusing if the impact isn’t clear — what should I do when the system is 85.8% certain vs. 87% certain?

    - **Showing confidence could create mistrust**. If the confidence level could be misleading for less-savvy users, reconsider how it’s displayed, or whether to display it at all. A misleadingly high confidence, for example, may cause users to blindly accept a result.
    
### Decide how best to show model confidence
If your research confirms that displaying model confidence improves decision making, the next step is choosing an appropriate visualization.
Types of visualizations include:
    - **Categorical:** These visualizations categorize confidence values into buckets, such as High / Medium / Low and show the category rather than the numerical value.
    - **N-best alternatives:** Rather than providing an explicit indicator of confidence, the system can display the N-best alternative results. For example, “This photo might be of New York, Tokyo, or Los Angeles.”
    - **Numeric:** A common form of this is a simple percentage. Numeric confidence indicators are risky because they presume your users have a good baseline understanding of probability.
    - **Data visualizations:** There are graphic-based indications of certainty. Keep in mind, however, that some common data visualizations are best understood by expert users in specific domains.
    
**Key concept**
To assess whether or not showing model confidence increases trust and makes it easier for people to make decisions, you can conduct user research with people who reflect the diversity of your audience.