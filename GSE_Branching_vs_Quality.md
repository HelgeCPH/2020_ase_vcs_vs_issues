# Welcome to Advanced Software Engineering

## Global Software Engineering in Open Source and its Effect on Quality

![](https://comidoc.net/static/assets/thumbs/480/webp/2267906_505c.webp)

## Learning Objectives

After this session (+ exercises) the student will be able to:

  * Understand how research analyzing VCS histories and issue trackers collects the underlying data.
  * Analyze the history from Git repositories and the Jira issue tracker.
  * Apply scripts and programs in various languages to clean and pre-process the exported data.
  * Apply scripts and programs in various languages to analyze Git VCS data and Jira issue tracker data with respect to certain hypotheses/research questions.
  * Interpret the analysis results to either better understand current practices or to suggest actionable changes of current practices in software engineering.
  
-----------

# What are we doing today?

## Motivation

You all read the two following papers:

  * E. Shihab et al. ["The Effect of Branching Strategies on Software Quality"](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/shihab-esem-2012.pdf)
  * M. Cataldo et al. ["Software Dependencies, Work Dependencies, and Their Impact on Failures"](https://www.researchgate.net/profile/Jeffrey_Roberts2/publication/220070820_Software_Dependencies_Work_Dependencies_and_Their_Impact_on_Failures/links/0046352651c19d5aef000000/Software-Dependencies-Work-Dependencies-and-Their-Impact-on-Failures.pdf))

---------

## Discussion


### What did you take away from the papers?

#### a) "The Effect of Branching Strategies on Software Quality"

  *
  *

#### b) "Software Dependencies, Work Dependencies, and Their Impact on Failures"

  *
  *

### What was the method that was applied in the research?

### What are the key results?



-----------



# Recap: Git Branching

Many VCS have some form of branching support. Branching means to diverge from the main line of development and continue to do work without messing with that main line. In many VCSs, this is an expensive process, often requiring you to create a new copy of your source code directory, which can take a long time for large projects.

Some people refer to the branching model in Git as its _killer feature_. The way Git branches is incredibly lightweight, making branching operations nearly instantaneous and switching back and forth between branches generally just as fast. Git encourages a workflow that branches and merges often.

## What is a Branch?


Git stores as a series of snapshots. 

When you commit in Git, it stores a commit object that contains a pointer to the snapshot of the content you staged, the author and message metadata, and zero or more pointers to the commit or commits that were the direct parents of this commit: 

  * _zero_ parents for the first commit
  * _one_ parent for a normal commit
  * _multiple_ parents for a commit that results from a merge of two or more branches

A _branch_ in Git is simply a pointer to a commit. The default branch name is `master`. Every time you commit, the pointer moves forward automatically.

![](http://git-scm.com/figures/18333fig0303-tn.png)


# Recap: Branching Strategies

  > “We are a team of four senior developers (by which I mean we’re all over 40 with 20+ years each of development experience) and not one of us has had a positive experience in the past with branching the mainline... The branch is easy - it’s the merge at the end that’s painful”.
  >
  >  [Phillips et al. _"Branching and Merging: An Investigation into Current Version Control Practices"_](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.278.6065&rep=rep1&type=pdf)



## Long-Running Branches/Branch by Release

Many Git developers have only code that is entirely stable in the `master` branch —possibly only code that has been or will be released. Another parallel branch named `develop` or `next` contains work to test for stability —it is not necessarily always stable, but whenever it gets to a stable state, it can be merged into `master`. It is used to pull in topic branches when they are ready.

In reality, we are talking about pointers moving up the line of commits. The stable branches are farther down the line in your commit history, and the bleeding-edge branches are farther up the history.


![](http://git-scm.com/figures/18333fig0318-tn.png)

That is, we can think about those branches as work silos, where sets of commits graduate to a more stable silo when they are fully tested.

![](http://git-scm.com/figures/18333fig0319-tn.png)


Figure 1. of [Walrad et al. _"The Importance of Branching Models in SCM"_](
https://www.researchgate.net/profile/Chuck_Walrad/publication/2955749_The_importance_of_branching_models_in_SCM/links/0c960536418f2f0da4000000/The-importance-of-branching-models-in-SCM.pdf)


## Topic Branches/Branch by Purpose

A topic branch is a short-lived branch that you create and use for a single particular feature or related work. You saw this in the last section with the `iss53` and `hotfix` branches.

![](http://git-scm.com/figures/18333fig0320-tn.png)


After merging `iss91v2` and `dumbidea` and throwing away the original `iss91` branch (losing commits C5 and C6) the repository's history looks as in the following:

![](http://git-scm.com/figures/18333fig0321-tn.png)

Figure 3. of [Walrad et al. _"The Importance of Branching Models in SCM"_](
https://www.researchgate.net/profile/Chuck_Walrad/publication/2955749_The_importance_of_branching_models_in_SCM/links/0c960536418f2f0da4000000/The-importance-of-branching-models-in-SCM.pdf)


## Git-Flow

Read on it here: http://nvie.com/posts/a-successful-git-branching-model/

![](http://nvie.com/img/git-model@2x.png)


## No Branches/Trunk-based Development

  > Almost all development occurs at the “head” of the repository​, not on branches. This helps identify integration problems early and minimizes the amount of merging work needed. It also makes it much easier and faster to push out security fixes.
  >
  > Henderson [_"Software Engineering at Google"_](https://arxiv.org/pdf/1702.01715.pdf)

#### Release Branches

![](https://trunkbaseddevelopment.com/trunk1a.png)

#### No Branches

![](https://trunkbaseddevelopment.com/trunk1b.png)

  > A release typically starts in a fresh workspace, by syncing to the change number of the latest “green” build (i.e. the last change for which all the automatic tests passed), and making a release branch. The release engineer can select additional changes to be “cherry-picked”, i.e. merged from the main branch onto the release branch. Then the software will be rebuilt from scratch and the tests are run. If any tests fail, additional changes are made to fix the failures and those additional changes are cherry-picked onto the release branch, after which the softwarewillberebuiltandthetestsrerun. Whenthetestsallpass,thebuiltexecutable(s)and data file(s) are packaged up. All of these steps are automated so that the release engineer need only run some simple commands, or even just select some entries on a menu-driven UI, and choose which changes (if any) to cherry pick.
  >
  > Henderson [_"Software Engineering at Google"_](https://arxiv.org/pdf/1702.01715.pdf)

  


## Other Branching Models

  * **Github-Flow**: http://scottchacon.com/2011/08/31/github-flow.html
  * Platform Branches http://www.creativebloq.com/web-design/choose-right-git-branching-strategy-121518344
  ![](http://cdn.mos.cms.futurecdn.net/4c32e6c4a3a45756ab06b9f54b904f69-650-80.jpg)

<!--
* New Feature Version Branches: https://ustwo.com/blog/branching-strategies-with-git/
  ![](https://usweb-cdn.ustwo.com/ustwo-production/uploads/2012/03/ustwo-branching-branching1.jpg)
  * http://www.kumaranuj.com/2015/11/gi-branching-strategies.html

-->


# Which Branching Model does Microsoft Use?

In the paper [_"The Effect of Branching Strategies on Software Quality"_](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/shihab-esem-2012.pdf) the authors describe how Microsoft used branches when building Windows 7 and Windows Vista.


Which branching model is it?


# Let's do some research!

![](images/your_turn.gif)

## RQ0: With which branching models are the studied SW systems built?

## RQ1: Is there a correlation between branching activity and SW quality?

Here, I mean number of bugs reported in an issue tracker as a proxy for SW quality. Moreover, by branching activity, I mean the amount of merge commits, since this is what E. Shihab et al. and Phillips et al. describe as the real issue.

## RQ2: Are there metrics, such as size of commit, number of developers working on it, or similar (you choose) that are possess a stronger correlation to SW quality compared to branching activity?

------

# What do we need to investigate these research questions?

## Some SW systems to study

I suggest that we have a look at three systems from the Apache Software Foundation:

  * [Apache Airflow](https://github.com/apache/airflow)
  * [Apache Camel](https://github.com/apache/camel)
  * [Apache Ignite](https://github.com/apache/ignite)

So clone these to your machines.

Of course, we can include any other system that you would like to study too! For simplicity, we need that they have a JIRA (or similar) issue tracker online.

### Something that corresponds to binaries in Shihab et al.

Let's use tagged versions for each of the systems as corresponding to binaries.

How do we get these?

### History of each system

How do we get these?

An example with PyDriller, see `code_snippets/git_to_png.py`:

```python
from pydriller import RepositoryMining


REPO_NAME = "ignite"
FROM = "2a35fb6f02d6031e7f7b6a61e01579c48c081a67"
TO = "383273e3f66f702de2482466dce954d570a8ccf2"

    
cmd = f"git clone git@github.com:apache/{REPO_NAME}.git"
subprocess.run(cmd.split())
rm = RepositoryMining(REPO_NAME, from_commit=FROM, to_commit=TO)
for commit in rm.traverse_commits():
    print(f"{commit.hash[:10]}")
```

See the complete PyDriller documentation: https://pydriller.readthedocs.io/en/latest/

Let's analyze history between tagged version commits as constituents of this version.

![](images/ignite_1.5_1.6.png)

## Collecting all Tags/Releases

For each repo, we need all tagged releases to find commits that "belong" to a version.

```python
import os
from github import Github


ENV_NAME = 'GITHUB_API_KEY'
gh = Github(login_or_token=os.getenv(ENV_NAME))

tags = [t for t in gh.get_organization("apache").get_repo("ignite").get_tags()]
print(tags[0].name, tags[0].commit.sha)
```


## Failure Statistics

All three projects rely on JIRA as issue tracker.

Let's use bugs in versions as a proxy for SW quality.

  * [Apache Airflow JIRA](https://issues.apache.org/jira/projects/AIRFLOW/issues)
  * [Apache Camel JIRA](https://issues.apache.org/jira/projects/CAMEL/issues)
  * [Apache Ignite JIRA](https://issues.apache.org/jira/projects/IGNITE/issues)


How do we get these?

```python
import requests


JIRA_API_BASE_URL = "https://issues.apache.org/jira/"
PAGE_LENGTH = 500

proj_jira_id = "AIRFLOW"
start_idx = 0
url = (
    JIRA_API_BASE_URL
    + f"rest/api/2/search?jql=project={proj_jira_id}+order+by+created"
    + f"&issuetypeNames=Bug&maxResults={PAGE_LENGTH}&"
    + f"startAt={start_idx}&fields=id,key,priority,labels,versions,"
    + "status,components,creator,reporter,issuetype,description,"
    + "summary,resolutiondate,created,updated"
)
r = requests.get(url)
r_dict = r.json()
print(r_dict)
```

See JIRA API docs:

  * https://developer.atlassian.com/server/jira/platform/jira-apis-32344053/
  * https://docs.atlassian.com/DAC/rest/jira/6.1.html
  
# Plotting 2D Data

See Matplotlib's official documentation: https://pythonspot.com/matplotlib-scatterplot/


```python
import matplotlib.pyplot as plt


x_data = list(range(10, 100))
y_data = list(range(100, 10, -1))

# Plot
plt.scatter(x_data, y_data, alpha=0.5)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

### Plotting a correlation matrix

With pandas and matplotlib it could be:


```python
import matplotlib.pyplot as plt

plt.matshow(dataframe.corr())
plt.show()
```

# Computing Correlations

Likely Spearman's ρ is a good correlation coefficient to compute


```python
from scipy import stats


ρ, p = stats.spearmanr([1,2,3,4,5], [5,6,7,8,7])
print(ρ, p)
```

See the documentation of SciPy's implementation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html
or Pandas' documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html


# Who is doing what now?

Work in teams of two on one of the sub-tasks 


# Results???








