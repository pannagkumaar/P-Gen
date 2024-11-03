# P-Gen - Personalised Password List Generator

P-Gen is a Python-based tool for generating password lists based on provided information about the target. It can help security professionals and ethical hackers to create custom password lists for password cracking and security testing.

## Features

- Generate password lists based on target information.
- Include LeetSpeak (leet) password variations.
- Add numbers and years to passwords.
- Generate passwords by concatenating common words.
- Create passwords based on common keyboard patterns.
- Generate passwords using common phrases.
- Generate random passwords.
- Organize passwords into an output folder..

## Prerequisites

- Python 3.x
- Required Python libraries (can be installed using `pip`):
  - argparse
  - itertools

## Usage

- Clone the repository:

   ```bash
   git clone https://github.com/pannagkumaar/P-Gen.git
   cd P-Gen
    ```
- Run the script with desired options:    
   
   ```bash 
   python P-Gen.py -l -n -y -c -k -p -r
   ```
    - **-l** or **--leet**: Generate LeetSpeak passwords.  
    - **-n** or **--numbers**: Add numbers to the generated passwords.  
    - **-y** or **--years**: Add years to the generated passwords.  
    - **-c** or **--concatenate**: Generate passwords by concatenating common words.  
    - **-k** or **--keyboard**: Generate passwords based on common keyboard patterns.     
    - **-p** or **--phrases**: Generate passwords using common phrases.   
    - **-r** or **--random**: Generate random passwords.  

## Examples
- To generate LeetSpeak passwords with numbers and years:

```bash 
python P-Gen.py -l -n -y
```
- To generate passwords based on common phrases:
```bash 
python P-Gen.py -p
```


## Target Audience

P-Gen is ideal for the following audiences:

- **Penetration Testers**: Security professionals conducting penetration tests can use P-Gen to create password lists based on target information, improving their chances of identifying weak passwords.

- **Red Teamers**: Red teamers simulating real-world attacks can benefit from P-Gen to generate password lists that mimic potential targets' password choices.

- **Security Enthusiasts**: Cybersecurity enthusiasts and hobbyists can use P-Gen to experiment with password cracking techniques and enhance their knowledge of password security.

## Purpose

The primary purpose of P-Gen is to assist in:

- **Strengthening Security**: By enabling the generation of custom password lists, P-Gen helps identify and rectify weak password vulnerabilities, ultimately enhancing overall system security.

- **Security Awareness**: P-Gen can be used to raise awareness about password security and the importance of strong, unique passwords among end-users and organizations.
