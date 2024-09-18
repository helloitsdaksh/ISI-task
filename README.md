# ISI - task


## Task Overview: 

### Objective:
1.	Access a JSON file from the NOAA dataset page. **[DONE]**
2.	Extract certain information (latitude/longitude, file URL, and variable names) from the JSON. **[DONE]**
3.	Download the data from the file URL and parse it into a Pandas DataFrame. **[DONE]**
4.	Use the ISI table understanding pipeline to analyze the table blocks and detect variables. **[Partially DONE]**
5.	Validate the solution with multiple datasets. **[TODO: If Objective 4 is achieved]**

Setup Process

1.	Environment Setup:
   * Hardware: Macbook pro M2 pro.
   * Software: DataSpell IDE, miniforge, conda, Python.
   * Dependencies: Installed as per the mac_m1.yml file from envs in the Github Repo.
   
2.	Changes made to run the setup: **[Changes marked in bold]**

  * **README.md:** 
      #### Setting up virtual environment
      * Install conda for package management: [conda miniforge](https://github.com/conda-forge/miniforge)
      * **Please run this command running the further steps `conda config --set ssl_verify no`**
      * Platform specific environment files are present in `envs` directory
      * **Make sure you run every command from the root directory of the GitHub repo which is ./isi-table-understanding**
      * Setup virtual env by running: `make setup-conda-env ENVIRONMENT=<platform name>`
      * Destroy conda env by running: `make destroy-conda-env`
        
  * **Envs**
    #### Setting up the env from mac_m1.yml file:
        name: table-understanding-venv
        channels:
          - conda-forge
        dependencies:
          - python=3.8.* ...
  * **MakeFile**
      #### Removing python_version from make file command:
        * `setup-conda-env:
    	@[ "${ENVIRONMENT}" ] || ( echo ">> Error: ENVIRONMENT is not set"; exit 1 )
    	@conda env create --file ./envs/$(ENVIRONMENT).yml;`
    
3. TODO: After making the changes commands to run:
   * Download this file and extract it into (./tmp):
     *  How to order the files:
       * `./isi-table-understanding/tmp/psl/psl.tar.gz`
       * `./isi-table-understanding/tmp/glove/glove.840B.300d.zip`
       * `./isi-table-understanding/InferSent` **[Clone this from the link mentioned]**

   * RUN: `make run PIPELINE=psl`
     *   This actually starts running the code but gives out the error.
       * `pydoc.ErrorDuringImport: problem in cell_classifier.psl_cell_classifier - ValueError: numpy.ndarray size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
make: *** [run] Error 1`
       * **Not able to do further error debugging since not sure what exactly is going wrong.**

4.   **Added Code for Successful Objective 1,2,3:** 
 
 
