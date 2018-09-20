'''
Created on September 20, 2018
@author: Caroline Telma
I pledge my honor that I have abided by the Stevens Honor System.
'''
import unittest
from GitHubAPI import RepositoryNames, CommitNumber

class TestGithub(unittest.TestCase):

    def testRepository_1(self):
        allRepos = RepositoryNames('richkempinski')
        self.assertGreaterEqual(len(allRepos), 4)
        self.assertIn('hellogitworld',allRepos)
        self.assertIn('helloworld',allRepos)
        self.assertIn('Project1',allRepos)
        self.assertIn('threads-of-life',allRepos)

    def testRepository_2(self):
        allRepos = repoNames('ctelma')
        self.assertGreaterEqual(len(allRepos), 4)
        self.assertIn('GitHubAPI567',allRepos)
        self.assertIn('helloworld',allRepos)
        self.assertIn('SSW-567-HW01',allRepos)
        self.assertIn('Triangle567',allRepos)

    def testNumberCommits_1(self):
        self.assertGreaterEqual(commitNum('ctelma','helloworld'),2)

    def testNumberCommits_2(self):
        self.assertGreaterEqual(commitNum('richkempinski','hellogitworld'),30)

    def testInvalidUsername(self):
        allRepos = RepositoryNames('ctelm')
        self.assertEqual(len(allRepos), 0)
