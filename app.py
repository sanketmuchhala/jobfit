from flask import Flask, request, jsonify, render_template
import re
import spacy
from transformers import pipeline
import os

app = Flask(__name__)

# Load pre-trained model for keyword extraction
nlp_transformers = pipeline("ner", model="dslim/bert-base-NER")

# Check if SpaCy model is installed, if not, download it
try:
    nlp_spacy = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp_spacy = spacy.load("en_core_web_sm")
    
# Predefined list of technical keywords
technical_keywords = [
    'Python', 'Java', 'JavaScript', 'TypeScript', 'C', 'C++', 'C#', 'Ruby', 'PHP', 'Go', 'Swift', 'Kotlin', 'Rust', 'R', 'Scala', 'Perl', 'Haskell', 'Matlab', 'SAS',
    'HTML', 'CSS', 'SASS', 'LESS', 'XML', 'JSON', 'YAML',
    'SQL', 'MySQL', 'PostgreSQL', 'SQLite', 'Oracle', 'MongoDB', 'Cassandra', 'Redis', 'Elasticsearch', 'Firebase', 'MariaDB', 'DynamoDB',
    'React', 'Angular', 'Vue.js', 'Svelte', 'Ember.js', 'Backbone.js', 'jQuery', 'Bootstrap', 'D3.js', 'Three.js',
    'Node.js', 'Express.js', 'Koa.js', 'NestJS',
    'Django', 'Flask', 'FastAPI', 'Spring Boot', 'Ruby on Rails', 'Laravel', 'ASP.NET', 'Meteor.js', 'Next.js', 'Nuxt.js',
    'TensorFlow', 'Keras', 'PyTorch', 'Theano', 'Caffe', 'MXNet', 'Chainer', 'CNTK', 'Torch',
    'scikit-learn', 'Pandas', 'NumPy', 'SciPy', 'Matplotlib', 'Seaborn', 'NLTK', 'Spacy', 'Gensim', 'OpenCV',
    'Hadoop', 'Spark', 'Kafka', 'Hive', 'Pig', 'Storm', 'Flink', 'Samza', 'HBase', 'Presto',
    'AWS', 'Azure', 'Google Cloud', 'IBM Cloud', 'Oracle Cloud', 'DigitalOcean', 'Heroku', 'Firebase', 'Netlify', 'Vercel',
    'Docker', 'Kubernetes', 'OpenShift', 'Mesos', 'Swarm', 'Vagrant', 'Terraform', 'Ansible', 'Chef', 'Puppet', 'SaltStack',
    'Git', 'GitHub', 'GitLab', 'Bitbucket', 'SVN', 'Mercurial',
    'Jenkins', 'Travis CI', 'CircleCI', 'TeamCity', 'Bamboo', 'GitHub Actions', 'GitLab CI', 'Drone CI', 'GoCD',
    'Linux', 'Unix', 'Windows', 'MacOS', 'Ubuntu', 'Debian', 'Fedora', 'CentOS', 'Red Hat', 'Arch Linux', 'FreeBSD', 'OpenBSD',
    'Bash', 'Shell', 'Powershell', 'Zsh',
    'Agile', 'Scrum', 'Kanban', 'XP', 'Lean', 'SAFe',
    'Jira', 'Trello', 'Asana', 'Basecamp', 'ClickUp', 'Monday.com', 
    'Figma', 'Sketch', 'Adobe XD', 'InVision', 'Marvel', 'Zeplin', 'Balsamiq',
    'Tableau', 'Power BI', 'Looker', 'QlikView', 'Domo', 'Sisense',
    'Salesforce', 'SAP', 'Oracle ERP', 'Microsoft Dynamics', 'NetSuite', 'Workday',
    'Blockchain', 'Ethereum', 'Hyperledger', 'Bitcoin', 'Solidity', 'Truffle', 'Ganache',
    'Cybersecurity', 'Penetration Testing', 'Ethical Hacking', 'Network Security', 'Information Security', 'Cryptography', 'SIEM', 'IDS', 'IPS',
    'Natural Language Processing', 'Computer Vision', 'Reinforcement Learning', 'Deep Learning', 'Machine Learning', 'Artificial Intelligence', 'Data Science', 'Big Data',
    'Business Intelligence', 'Data Warehousing', 'ETL', 'Data Engineering', 'Data Mining', 'Predictive Analytics', 'Statistics', 'Mathematics',
    'Augmented Reality', 'Virtual Reality', 'Mixed Reality', 'Game Development', 'Unity', 'Unreal Engine', 'Blender', 'Maya', '3ds Max',
    'Internet of Things', 'IoT', 'Embedded Systems', 'Microcontrollers', 'Arduino', 'Raspberry Pi', 'ESP32', 'Zigbee', 'Bluetooth Low Energy',
    'Robotics', 'Automation', 'Control Systems', 'ROS', 'PLC', 'SCADA',
    'Quantum Computing', 'Qiskit', 'IBM Q Experience', 'Microsoft Quantum', 'D-Wave'
]


def clean_text(text):
    # Clean the text by removing unwanted characters
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def extract_keywords(job_description):
    job_description = clean_text(job_description)

    # Use SpaCy for POS tagging
    doc = nlp_spacy(job_description)
    spacy_keywords = {token.text for token in doc if token.pos_ in {'NOUN', 'PROPN'}}

    # Use transformers for NER
    ner_results = nlp_transformers(job_description)
    transformer_keywords = {entity['word'] for entity in ner_results if entity['entity'].startswith("B-")}

    # Combine and filter keywords
    extracted_keywords = spacy_keywords.union(transformer_keywords)
    relevant_keywords = [kw for kw in extracted_keywords if kw in technical_keywords]
    
    return relevant_keywords

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract_keywords', methods=['POST'])
def get_keywords():
    job_description = request.form['job_description']
    keywords = extract_keywords(job_description)
    return jsonify({'keywords': keywords})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
