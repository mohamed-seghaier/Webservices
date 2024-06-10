# WEBSERVICES Project

## Project Members
- **ZIANE Akli**
- **BEN HSSAN Jaffar**
- **NANS Maurel**
- **SEGHAIER Mohamed-Ali**

## Installation Instructions

1. **Clone the Repository with Submodules**

     To get all submodules, run the following command:
     ```sh
     git clone --recurse-submodules git@github.com:mohamed-seghaier/Webservices.git

2. **Verify and Prepare the Update Script**

      Ensure that the ./update script is present and executable. If necessary, set the correct permissions:
  
      ```sh
      chmod +x ./update
      ```

3. **Check for Required Files**

      Verify that the following files exist:
    
        `./gitmodules`
        `./.scripts/update.py`
    
4. **Run the Update Script**

      Finally, execute the update script to complete the setup:
      ```sh
      ./update
      ```
