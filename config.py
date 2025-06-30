"""
Configuration file for TalentScout Hiring Assistant
Contains tech stack databases and question templates
"""

# Technology Keywords Database
TECH_KEYWORDS = {
    'programming_languages': [
        'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'csharp',
        'php', 'ruby', 'go', 'golang', 'rust', 'kotlin', 'swift', 'scala',
        'r', 'matlab', 'perl', 'shell', 'bash', 'powershell'
    ],
    'frontend_frameworks': [
        'react', 'angular', 'vue', 'vue.js', 'svelte', 'ember', 'backbone',
        'jquery', 'bootstrap', 'tailwind', 'material-ui', 'semantic-ui'
    ],
    'backend_frameworks': [
        'django', 'flask', 'fastapi', 'spring', 'spring boot', 'express',
        'node.js', 'laravel', 'symfony', 'rails', 'sinatra', 'gin', 'echo'
    ],
    'databases': [
        'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle',
        'sql server', 'cassandra', 'elasticsearch', 'firebase', 'dynamodb'
    ],
    'cloud_platforms': [
        'aws', 'azure', 'gcp', 'google cloud', 'heroku', 'digitalocean',
        'linode', 'vultr', 'cloudflare', 'netlify', 'vercel'
    ],
    'devops_tools': [
        'docker', 'kubernetes', 'jenkins', 'gitlab ci', 'github actions',
        'terraform', 'ansible', 'chef', 'puppet', 'nagios', 'prometheus'
    ],
    'data_science': [
        'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch', 'keras',
        'matplotlib', 'seaborn', 'plotly', 'jupyter', 'apache spark'
    ],
    'mobile_development': [
        'react native', 'flutter', 'ionic', 'xamarin', 'android', 'ios',
        'swift', 'kotlin', 'objective-c'
    ],
    'version_control': [
        'git', 'github', 'gitlab', 'bitbucket', 'svn', 'mercurial'
    ],
    'testing_tools': [
        'jest', 'pytest', 'junit', 'selenium', 'cypress', 'mocha', 'chai',
        'postman', 'insomnia', 'swagger'
    ]
}

# Comprehensive Question Database
QUESTION_TEMPLATES = {
    # Programming Languages
    'Python': [
        "What is the difference between list and tuple in Python?",
        "Explain Python's GIL (Global Interpreter Lock) and its implications.",
        "How do you handle exceptions in Python? Provide an example.",
        "What are Python decorators and how would you use them?",
        "Explain the difference between deep copy and shallow copy.",
        "What is the difference between __str__ and __repr__ methods?",
        "How does Python's garbage collection work?",
        "What are generators in Python and when would you use them?"
    ],
    'Java': [
        "What is the difference between JDK, JRE, and JVM?",
        "Explain the concept of polymorphism in Java with an example.",
        "What are the main principles of OOP in Java?",
        "What is the difference between abstract class and interface?",
        "Explain Java's memory management and garbage collection.",
        "What are the different types of inheritance in Java?",
        "How does exception handling work in Java?",
        "What is the significance of the 'final' keyword in Java?"
    ],
    'Javascript': [
        "What is the difference between == and === in JavaScript?",
        "Explain closures in JavaScript with an example.",
        "What is the event loop in JavaScript and how does it work?",
        "What are JavaScript promises and how do they work?",
        "Explain the concept of hoisting in JavaScript.",
        "What is the difference between var, let, and const?",
        "How does 'this' keyword work in JavaScript?",
        "What are arrow functions and how do they differ from regular functions?"
    ],
    'React': [
        "What is the difference between state and props in React?",
        "Explain the React component lifecycle methods.",
        "What are React Hooks and why are they useful?",
        "How does React's virtual DOM work?",
        "What is the difference between controlled and uncontrolled components?",
        "Explain React's Context API and when to use it.",
        "What are higher-order components (HOCs) in React?",
        "How do you optimize React application performance?"
    ],
    'Angular': [
        "What is the difference between Angular and AngularJS?",
        "Explain Angular's dependency injection system.",
        "What are Angular directives and their types?",
        "How does data binding work in Angular?",
        "What is the purpose of Angular services?",
        "Explain Angular's component lifecycle hooks.",
        "What is RxJS and how is it used in Angular?",
        "How do you handle forms in Angular?"
    ],
    'Vue': [
        "What is Vue.js and what are its key features?",
        "Explain Vue's reactivity system.",
        "What is the difference between v-if and v-show?",
        "How do you handle events in Vue.js?",
        "What are Vue components and how do they communicate?",
        "Explain Vue's lifecycle hooks.",
        "What is Vuex and when would you use it?",
        "How do you create custom directives in Vue?"
    ],
    'Node.js': [
        "What is the event-driven architecture in Node.js?",
        "Explain the difference between synchronous and asynchronous programming.",
        "What are callbacks, promises, and async/await in Node.js?",
        "How does Node.js handle concurrent requests?",
        "What is the purpose of package.json file?",
        "Explain Node.js modules and how they work.",
        "What are streams in Node.js?",
        "How do you handle errors in Node.js applications?"
    ],
    'Django': [
        "What is Django ORM and how does it work?",
        "Explain the MVC pattern in Django.",
        "What are Django middlewares and their use cases?",
        "How does Django handle database migrations?",
        "What is the difference between Django's forms and model forms?",
        "Explain Django's authentication system.",
        "What are Django signals and when would you use them?",
        "How do you optimize Django application performance?"
    ],
    'Flask': [
        "What is Flask and how does it differ from Django?",
        "Explain Flask's application context and request context.",
        "How do you handle routing in Flask?",
        "What are Flask blueprints and when would you use them?",
        "How do you handle database operations in Flask?",
        "What is Flask-SQLAlchemy and its benefits?",
        "How do you implement authentication in Flask?",
        "Explain Flask's templating system."
    ],
    'Spring': [
        "What is the Spring Framework and its core features?",
        "Explain dependency injection in Spring.",
        "What is the difference between @Component, @Service, and @Repository?",
        "How does Spring Boot simplify Spring development?",
        "What are Spring profiles and how do you use them?",
        "Explain Spring's transaction management.",
        "What is Spring MVC and how does it work?",
        "How do you handle exceptions in Spring applications?"
    ],
    'Express': [
        "What is Express.js and its key features?",
        "How do you handle routing in Express?",
        "What are Express middlewares and how do they work?",
        "How do you handle errors in Express applications?",
        "What is the difference between app.use() and app.get()?",
        "How do you implement authentication in Express?",
        "Explain Express's templating engines.",
        "How do you handle file uploads in Express?"
    ],
    # Databases
    'Mysql': [
        "What is the difference between INNER JOIN and LEFT JOIN?",
        "Explain database normalization and its types.",
        "What are indexes and how do they improve query performance?",
        "What is the difference between DELETE, DROP, and TRUNCATE?",
        "How do you optimize slow MySQL queries?",
        "What are stored procedures and their advantages?",
        "Explain ACID properties in database systems.",
        "What is the difference between MyISAM and InnoDB storage engines?"
    ],
    'Postgresql': [
        "What are the advantages of PostgreSQL over MySQL?",
        "Explain PostgreSQL's MVCC (Multi-Version Concurrency Control).",
        "What are PostgreSQL extensions and how do you use them?",
        "How do you handle JSON data in PostgreSQL?",
        "What are PostgreSQL's advanced data types?",
        "Explain PostgreSQL's indexing strategies.",
        "How do you perform database backup and recovery in PostgreSQL?",
        "What are PostgreSQL functions and procedures?"
    ],
    'Mongodb': [
        "What is MongoDB and how does it differ from relational databases?",
        "Explain MongoDB's document structure and collections.",
        "What are MongoDB indexes and their types?",
        "How do you perform aggregation in MongoDB?",
        "What is sharding in MongoDB?",
        "Explain MongoDB's replication mechanism.",
        "How do you handle transactions in MongoDB?",
        "What are the advantages and disadvantages of using MongoDB?"
    ],
    'Redis': [
        "What is Redis and what are its primary use cases?",
        "Explain Redis data structures and their applications.",
        "How does Redis handle persistence?",
        "What is Redis clustering and how does it work?",
        "How do you implement caching strategies with Redis?",
        "What are Redis pub/sub features?",
        "How do you handle Redis memory optimization?",
        "What are Redis transactions and Lua scripts?"
    ],
    # Cloud Platforms
    'Aws': [
        "What are the core AWS services you've worked with?",
        "Explain the difference between EC2 and Lambda.",
        "What is AWS S3 and its common use cases?",
        "How do you implement auto-scaling in AWS?",
        "What is the difference between EBS and EFS?",
        "Explain AWS VPC and its components.",
        "How do you monitor AWS resources?",
        "What are AWS security best practices?"
    ],
    'Azure': [
        "What are the key Azure services for web applications?",
        "Explain Azure's resource management hierarchy.",
        "What is the difference between Azure VMs and App Service?",
        "How do you implement CI/CD with Azure DevOps?",
        "What are Azure storage options and their use cases?",
        "Explain Azure's identity and access management.",
        "How do you monitor Azure applications?",
        "What are Azure's disaster recovery options?"
    ],
    'Gcp': [
        "What are the main Google Cloud Platform services?",
        "Explain the difference between Compute Engine and App Engine.",
        "What is Google Cloud Storage and its storage classes?",
        "How do you implement auto-scaling in GCP?",
        "What are GCP's BigData and ML services?",
        "Explain GCP's networking concepts.",
        "How do you manage security in Google Cloud?",
        "What are GCP's monitoring and logging tools?"
    ],
    # DevOps Tools
    'Docker': [
        "What is Docker and how does it differ from virtual machines?",
        "Explain the difference between Docker images and containers.",
        "What is a Dockerfile and its key instructions?",
        "How do you manage multi-container applications with Docker?",
        "What are Docker volumes and their types?",
        "Explain Docker networking concepts.",
        "How do you optimize Docker images for production?",
        "What are Docker security best practices?"
    ],
    'Kubernetes': [
        "What is Kubernetes and its key components?",
        "Explain the difference between Pods, Services, and Deployments.",
        "What are Kubernetes namespaces and their purpose?",
        "How do you handle configuration management in Kubernetes?",
        "What are Kubernetes ingress controllers?",
        "Explain Kubernetes scaling mechanisms.",
        "How do you monitor Kubernetes clusters?",
        "What are Kubernetes security best practices?"
    ],
    'Jenkins': [
        "What is Jenkins and its role in CI/CD?",
        "Explain Jenkins pipeline and its types.",
        "How do you configure Jenkins for automated builds?",
        "What are Jenkins plugins and their importance?",
        "How do you implement parallel builds in Jenkins?",
        "What are Jenkins agents and how do they work?",
        "How do you handle Jenkins security?",
        "What are Jenkins best practices for large teams?"
    ],
    # Data Science
    'Pandas': [
        "What is Pandas and its core data structures?",
        "How do you handle missing data in Pandas?",
        "Explain Pandas groupby operations.",
        "What are the different ways to merge DataFrames?",
        "How do you optimize Pandas performance for large datasets?",
        "What are Pandas indexing and selection methods?",
        "How do you handle time series data in Pandas?",
        "What are the best practices for data cleaning with Pandas?"
    ],
    'Numpy': [
        "What is NumPy and its advantages over Python lists?",
        "Explain NumPy array broadcasting.",
        "What are NumPy's mathematical and statistical functions?",
        "How do you perform array manipulations in NumPy?",
        "What is vectorization in NumPy?",
        "Explain NumPy's linear algebra capabilities.",
        "How do you handle large arrays efficiently in NumPy?",
        "What are NumPy's random number generation features?"
    ],
    'Tensorflow': [
        "What is TensorFlow and its key components?",
        "Explain TensorFlow's computation graph.",
        "What are TensorFlow sessions and eager execution?",
        "How do you build neural networks with TensorFlow?",
        "What is the difference between tf.keras and core TensorFlow?",
        "How do you handle data preprocessing in TensorFlow?",
        "What are TensorFlow's deployment options?",
        "How do you optimize TensorFlow models for production?"
    ],
    'Pytorch': [
        "What is PyTorch and how does it differ from TensorFlow?",
        "Explain PyTorch tensors and automatic differentiation.",
        "What are PyTorch datasets and data loaders?",
        "How do you build custom neural networks in PyTorch?",
        "What is PyTorch's dynamic computation graph?",
        "How do you implement transfer learning in PyTorch?",
        "What are PyTorch's optimization algorithms?",
        "How do you deploy PyTorch models?"
    ]
}

# General technical questions for unknown tech stacks
GENERAL_QUESTIONS = [
    "Describe a challenging technical problem you've solved recently and your approach.",
    "How do you stay updated with new technologies and best practices in your field?",
    "What's your approach to debugging complex issues in your code?",
    "How do you ensure code quality and maintainability in your projects?",
    "Describe your experience with version control systems and collaborative development.",
    "How do you approach performance optimization in your applications?",
    "What testing strategies do you use in your development process?",
    "How do you handle security considerations in your applications?"
]

# Position-specific question weights
POSITION_TECH_MAPPING = {
    'frontend': ['react', 'angular', 'vue', 'javascript', 'typescript', 'html', 'css'],
    'backend': ['python', 'java', 'node.js', 'django', 'spring', 'express'],
    'fullstack': ['react', 'node.js', 'python', 'javascript', 'django', 'express'],
    'data': ['python', 'pandas', 'numpy', 'tensorflow', 'pytorch', 'mysql', 'postgresql'],
    'devops': ['docker', 'kubernetes', 'aws', 'jenkins', 'terraform', 'ansible'],
    'mobile': ['react native', 'flutter', 'swift', 'kotlin', 'android', 'ios']
}

# Application settings
APP_CONFIG = {
    'max_questions': 5,
    'min_questions': 3,
    'session_timeout': 3600,  # 1 hour in seconds
    'max_tech_stack_items': 10,
    'conversation_stages': [
        "greeting",
        "name_collection",
        "email_collection", 
        "phone_collection",
        "experience_collection",
        "position_collection",
        "location_collection",
        "tech_stack_collection",
        "technical_questions",
        "conclusion"
    ]
}

# UI Configuration
UI_CONFIG = {
    'primary_color': '#667eea',
    'secondary_color': '#764ba2',
    'success_color': '#4caf50',
    'warning_color': '#ff9800',
    'error_color': '#f44336',
    'background_color': '#f8f9fa'
}