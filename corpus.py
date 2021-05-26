# Define corpus words lists and dictionaries.

glows_pre = [
    'excellent work', 'fantastic job', 'great job', 'wonderful job', 'great effort', 'astounding work',
    'awesome job', 'nice work', 'terrific job', 'amazing job',
]

grows_pre = [
    'Going forward', 'Next time', 'As you continue your work as a writer', 'Moving on',
    'As you continue writing', 'For your next text', 'In the future', 'Looking forward',
    'Something to keep in mind', 'As you move on', 'One suggestion I have',
]

grows_effort = [
    'try to work on', 'try paying more attention to', 'consider how you could improve',
    'think about how you could work on', 'consider practicing', 'try to improve your skill of',
    'think of some ways you could improve', 'think about how your writing would be different if you could improve',
]

# Each key will be associated with a choice within a GUI.
skills_dict = {
    'Being Creative': ['producing creative and original ideas in your work',
                       'writing creatively and originally', 'keeping your ideas unique and fresh'],
    'Choosing Strong Evidence': ['selecting accurate and relevant text evidence to support writing',
                                 'using strong evidence that supports your work well',
                                 'choosing particularly strong evidence to support your writing'],
    'Citing Evidence': ['citing evidence from the text', 'citing text evidence', 'using text evidence'],
    'Clear Claim': ['making your claim clear to the reader', 'stating a clear claim that is straightforward',
                    'clearly stating a claim that the reader can understand'],
    'Complete introduction': ['producing a complete introduction that neatly summarizes writing',
                              'creating a particularly straightforward introduction',
                              'writing an introduction that neatly overviews your writing'],
    'Describing Connections': ['describing the connections between your ideas and the text',
                               'making the connections between your ideas especially clear to the reader',
                               'establishing strong connections between your written ideas'],
    'Explaining Evidence': ['explaining the connection between ideas and quotes used',
                            'thoroughly explaining how your evidence pertains to your ideas',
                            'clearly explaining your use of evidence as it pertains to your ideas'],
    'Explaining Ideas': ['explaining your ideas thoroughly throughout your writing',
                         'making your ideas especially clear to the reader', 'explaining your written thoughts'],
    'Organizing Handwriting': ['making your handwriting organized', 'organizing your handwriting',
                               'keeping your handwriting especially organized and neat',
                               'keeping your paragraphs neet and well separated'],
    'Proofreading': ['proofreading your work for errors in spelling and punctuation',
                     'carefully rereading your work for proofreading errors',
                     'looking over your paper for errors in grammar, spelling and punctuation'],
    'Providing Background Information': ['providing background information about what you\'re writing',
                                         'providing the reader with relevant background information',
                                         'supporting your writing with useful background information'],
    'Theme': ['stating a relevant and insightful theme', 'developing and stating a theme in your writing',
              'pointing out a relevant theme and explaining it to the reader'],
    'Transitions': ['adding transitions at the beginning and ends of your paragraphs',
                    'using effective and seamless transitions throughout your writing',
                    'creating smooth transitions to segue between your ideas'],
    'Using R-A-C-E': ['masterfully using the R-A-C-E Strategy throughout your work',
                      'aligning your text evidence well by using the R-A-C-E Strategy',
                      'using the R-A-C-E Strategy to keep your evidence citations organized'],
    'Vocabulary Usage': ['selecting and utilizing high-level vocabulary throughout your work',
                         'using an excellent array of vocabulary throughout your work',
                         'selecting meaningful and articulate-sounding vocabulary in your work'],
    'Writer\'s Voice': ['incorporating your own "writer\'s voice" throughout your work',
                        'creatively expressing your ideas using your own unique voice',
                        'keeping your ideas original-sounding, with unique phrasing'],
}
