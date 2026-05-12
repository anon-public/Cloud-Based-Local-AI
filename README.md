# Cloud-Based Local AI (Private AI)



## Table of Contents

- [Project Precis](#Project-Precis)
- [Tech Stack](#Tech-Stack)
- [Google Drive Setup](#Google-Drive-Setup)
- [Setting up the model](#Setting-up-the-model)
- [Request Workflow on Colab Environment](#Request-Workflow-on-Colab-Environment)
- [Getting Started](#Getting-Started)
---

## Project Precis

This repository aims to run an AI model 'Gamma4:latest' using cloud resources on Google Colab and while protects data privacy.
Colab provides a free NVIDIA T4 GPU (16 GB VRAM) which delivers 20 to 40 tokens per second for Gemma 4 and others models can also be used by this methodology while requirements should meet the colab resources for effective output.Can also shift towards Oracle Database however slower performance will be observed due to no GPU.

<div align='center'>
<img  width="558" height="246" alt="image" src="https://github.com/user-attachments/assets/6d401114-6379-4ff4-9f1f-3f62b90db3ad" />
<p><i>Here is a breakdown of both platforms</i></p>
</div>


## Tech Stack

<div align='center'>
<img width="563" height="439" alt="image" src="https://github.com/user-attachments/assets/bf0153e0-686d-42e4-9d5b-a391379a2766" />
</div>

## Google Drive Setup
These steps are performed once in a browser. They configure the services and files that persist across Colab sessions via Google Drive.
Create thse files in your specific drive with the main folder named as 'Local AI Model' :
<ul>
  <li>Config - Add .env, .model and FastAPI middleware files in it</li>
  <li>Backup - To save chat history</li>
  <li>models - Cached AI model</li>
</ul>


#### Dotenv file
Add the required API keys for cloudflare, open webui and random hex string for FastAPI. Also add the custom domain and Brand Name for the Private AI model.Add this file in Drive > Local AI Model > config.
<div align='center'>
  <img width="443" height="265" alt="image" src="https://github.com/user-attachments/assets/b5cf337c-ffa9-4bda-869d-defe7b71defc" />
<p><i>Preview of .env file</i></p>
</div>

#### Model File
Save this as gemma4-params.modelfile in Drive > gemma4-colab > config. It sets inference quality defaults for Gemma 4 specifically.Add this file in Drive > Local AI Model > config.
A sample system prompt is provided which can be alter if needed.
<div align='center'>
<img width="1570" height="226" alt="image" src="https://github.com/user-attachments/assets/126e4cd9-4b4f-4dc8-865a-bedd355e4491" />
<p><i>Preview of .Modelfile file</i></p>
</div>

#### FastAPI Middleware
The FastAPI middleware sits between the public tunnel and Ollama, adding API key authentication and request logging.The file is provided above which should be added at Drive > Local AI Model > config.

## Setting up the model
### Running Jupiter Notebook
Run from cell 1 - 10 in the Source Code.ipynb to start up the model and run cell 11 when ending the session to save chat history in the drive for further retrieval. Connect your specific Google Drive account to access the Model and cached files from the drive in Google Colab environment.The cell 9 keeps by session alive by using a small JavaScript function.
Reference Steps for running the notebook:
<ol>
  <li>Open Colab notebook (Source Code.ipynb) in browser
  <li>Set runtime type to T4 GPU (Runtime > Change runtime type)</li>
  <li>Run Cell 1: Mount Google Drive</li>
  <li>Run Cell 2: Load .env</li>
  <li>Run Cell 3: Install dependencies (~3 to 4 min on fresh session)</li>
  <li>Run Cell 4: Start Ollama server</li>
  <li>Run Cell 5: Restore model from Drive (30 sec if cached, 15 min if not)</li>
  <li>Run Cell 6: Start FastAPI middleware</li>
  <li>Run Cell 7: Start Open WebUI</li>
  <li>Run Cell 8: Start Cloudflare Tunnel or Ngrok</li>
  <li>Run Cell 9: Start browser keep-alive</li>
  <li>Run Cell 10: Verify all services and test inference</li>
  <li>Share the URL with any users who need access</li>
</ol>


## Request Workflow on Colab Environment
### User -> Model
<div align='center'>
<img width="496" height="443" alt="image" src="https://github.com/user-attachments/assets/8d4cdee4-9d84-4513-97b8-44175e0b1225" />
<p><i>Preview of user to model request workflow</i></p>
</div>

### Model -> User
<div align='center'>
<img width="498" height="250" alt="image" src="https://github.com/user-attachments/assets/921ddb47-f757-443e-a4fe-bb0c4f16f9f7" />
<p><i>Preview of model to user request workflow</i></p>
</div>

### Data Privacy
<div align='center'>
<img width="496" height="149" alt="image" src="https://github.com/user-attachments/assets/61f705d9-bd14-4094-a106-97bf3862a19e" />
</div>

>Important: Unlike Oracle Cloud where all inference happens on hardware you control, Google Colab runs on Google's servers. Your prompts pass through Google's infrastructure during inference. For strictly confidential use, revert to Oracle Cloud or a local machine with GPU.

## Getting Started
Follow these steps to setup your Private AI model
### Fork a repository
```bash
git clone https://github.com/YourUsername/Cloud-Based-Local-AI.git
cd Cloud-Based-Local-AI
```

### Create a new Branch
```bash
git branch new_feature_update
git checkout new_feature_update
```

### Create a Pull request
After committing and pushing the changes to the fork repository create a Pull Request. Provide a clear description of your additions and submit.

## License
This project is governed by MIT License which gives the rights to use,copy modify and distribute this code for any purpose residing in the License terms which are mentioned in LICENSE.md file. The only requirements are that you retain the original copyright and license notice when you distribute the software. We provide this code "as is" with no warranty.
>Note: This summary is for informational purposes only and does not constitute legal advice. Always review the full text of the MIT License for official legal understanding.
