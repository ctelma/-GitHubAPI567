'''
Created on September 20, 2018
Updated on September 30, 2018
@author: Caroline Telma
I pledge my honor that I have abided by the Stevens Honor System.
'''
import unittest
from unittest import mock
import GitHubAPI

class TestGithub(unittest.TestCase):

    @mock.patch('TestGitHubAPI.RepositoryNames')
    def testRepo1(self, mock_repo_names):
         mock_repo_names.return_value = ["hellogitworld", "helloworld", "Project1", "threads-of-life"]

         allRepos = RepositoryNames('richkempinski')
         self.assertGreaterEqual(len(allRepos), 4)
         self.assertIn('hellogitworld',allRepos)
         self.assertIn('helloworld',allRepos)
         self.assertIn('Project1',allRepos)
         self.assertIn('threads-of-life',allRepos)



    @mock.patch('TestGitHubAPI.RepositoryNames')
    def testRepo2(self, mock_repo_names):
        mock_repo_names.return_value = ['GitHubAPI567','helloworld', 'SSW-567-HW01','Triangle567']

        allRepos = RepositoryNames('ctelma')
        self.assertGreaterEqual(len(allRepos), 4)
        self.assertIn('GitHubAPI567',allRepos)
        self.assertIn('helloworld',allRepos)
        self.assertIn('SSW-567-HW01',allRepos)
        self.assertIn('Triangle567',allRepos)


    @mock.patch('TestGitHubAPI.CommitNumber')
    def testNummberCommits1(self, mock_commit_number):
        mock_commit_number.return_value = 30
        self.assertEqual(CommitNumber("richkempinski", "hellogitworld"),30)
        mock_commit_number.return_value = 2
        self.assertEqual(CommitNumber("richkempinski", "helloworld"),2)
        mock_commit_number.return_value = 1
        self.assertEqual(CommitNumber("richkempinski", "threads-of-life"),1)

    @mock.patch('TestGitHubAPI.RepositoryNames')
    def testInvalidUsername(self, mock_repo_name):
        mock_repo_name.return_value = []
        allRepos = RepositoryNames('ctelm')
        self.assertEqual(len(allRepos), 0)

if __name__ == '__main__':
    print("Running unit test")
    unittest.main()
