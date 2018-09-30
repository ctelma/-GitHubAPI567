'''
Created on September 20, 2018
Updated on September 30, 2018
@author: Caroline Telma
I pledge my honor that I have abided by the Stevens Honor System.
'''
import unittest
import json
from GitHubAPI import RepositoryNames, CommitNumber
from unittest.mock import Mock, patch

class TestGithub(unittest.TestCase):

    @patch('TestGitHubAPI.RepositoryNames')
     def testRepo1(mock_repo_names, self):
         mock_repo_names.return_value = Mock(['richkempinski'])

         allRepos = RepositoryNames('richkempinski')
         self.assertGreaterEqual(len(allRepos), 4)
         self.assertIn('hellogitworld',allRepos)
         self.assertIn('helloworld',allRepos)
         self.assertIn('Project1',allRepos)
         self.assertIn('threads-of-life',allRepos)



    @patch('TestGitHubAPI.RepositoryNames')
    def testRepo2(mock_repo_names, self):
        fake_json = ['GitHubAPI567',
                     'helloworld',
                     'SSW-567-HW01',
                     'Triangle567',
                     'sq-com_example_standard-sqscanner-travis']
        mock_repo_names.return_value = Mock(fake_json)


        allRepos = RepositoryNames('ctelma')
        self.assertGreaterEqual(len(allRepos), 4)
        self.assertIn('GitHubAPI567',allRepos)
        self.assertIn('helloworld',allRepos)
        self.assertIn('SSW-567-HW01',allRepos)
        self.assertIn('Triangle567',allRepos)


    @patch('TestGitHubAPI.CommitNumber')
    def testNummberCommits1(mock_commit_number, self):
        mock_commit_number.return_value = Mock(2)
        self.assertGreaterEqual(CommitNumber('ctelma','helloworld'),2)

    @patch('TestGitHubAPI.CommitNumber')
    def testNummberCommits2(mock_commit_number, self):
        mock_commit_number.return_value = Mock(30)
        self.assertGreaterEqual(CommitNumber('richkempinski','hellogitworld'),30)

    @patch('TestGitHubAPI.RepositoryNames')
    def testInvalidUsername(mock_repo_name, self):
        mock_repo_name.return_value = Mock(0)
        allRepos = RepositoryNames('ctelm')
        self.assertEqual(len(allRepos), 0)

if __name__ == '__main__':
    print("Running unit test")
    unittest.main()
