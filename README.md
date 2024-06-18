# WEBSERVICES Project

## Project Members
- **ZIANE Akli**
- **BEN HSSAN Jaffar**
- **NANS Maurel**
- **SEGHAIER Mohamed-Ali**

### Needed
#### Windows
- **Python 3**
- **WSL or CYGWIN**  to run bash scripts | or just skip steps 3 and 4 by running the following command after the 2nd step, each time you want to pull or clone the project :

```sh
.scripts/update.py
```

#### GNU/Linux
Python3

## Installation Instructions

     

1. **Clone the Repository with Submodules**

     To get all submodules, run the following command:
     ```sh
     git clone --recurse-submodules git@github.com:mohamed-seghaier/Webservices.git
     ```

2. **Check for Required Files**

      Verify that the following files exist:
    
        `./gitmodules`
        `./.scripts/update.py`

4. **Verify and Prepare the Update Script**

      Ensure that the ./update script is present and executable. If necessary, set the correct permissions:
  
      ```sh
      chmod +x ./update
      ```
    
5. **Run the Update Script**

      Finally, execute the update script to complete the setup:
      ```sh
      ./update
      ```
