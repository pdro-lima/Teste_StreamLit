{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4b5e0007-a4f8-4a86-a1e9-f98beb37ee8d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Obtaining dependency information for streamlit from https://files.pythonhosted.org/packages/c5/ea/b50f166fb6e5c244568f798ade98fa261b82588ab9ad83230b327a82b42f/streamlit-1.31.1-py2.py3-none-any.whl.metadata\n",
      "  Downloading streamlit-1.31.1-py2.py3-none-any.whl.metadata (8.1 kB)\n",
      "Collecting altair<6,>=4.0 (from streamlit)\n",
      "  Obtaining dependency information for altair<6,>=4.0 from https://files.pythonhosted.org/packages/c5/e4/7fcceef127badbb0d644d730d992410e4f3799b295c9964a172f92a469c7/altair-5.2.0-py3-none-any.whl.metadata\n",
      "  Downloading altair-5.2.0-py3-none-any.whl.metadata (8.7 kB)\n",
      "Collecting blinker<2,>=1.0.0 (from streamlit)\n",
      "  Obtaining dependency information for blinker<2,>=1.0.0 from https://files.pythonhosted.org/packages/fa/2a/7f3714cbc6356a0efec525ce7a0613d581072ed6eb53eb7b9754f33db807/blinker-1.7.0-py3-none-any.whl.metadata\n",
      "  Downloading blinker-1.7.0-py3-none-any.whl.metadata (1.9 kB)\n",
      "Collecting cachetools<6,>=4.0 (from streamlit)\n",
      "  Obtaining dependency information for cachetools<6,>=4.0 from https://files.pythonhosted.org/packages/fb/2b/a64c2d25a37aeb921fddb929111413049fc5f8b9a4c1aefaffaafe768d54/cachetools-5.3.3-py3-none-any.whl.metadata\n",
      "  Downloading cachetools-5.3.3-py3-none-any.whl.metadata (5.3 kB)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: importlib-metadata<8,>=1.4 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (2.0.3)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (10.2.0)\n",
      "Collecting protobuf<5,>=3.20 (from streamlit)\n",
      "  Obtaining dependency information for protobuf<5,>=3.20 from https://files.pythonhosted.org/packages/ad/6e/1bed3b7c904cc178cb8ee8dbaf72934964452b3de95b7a63412591edb93c/protobuf-4.25.3-cp310-abi3-win_amd64.whl.metadata\n",
      "  Downloading protobuf-4.25.3-cp310-abi3-win_amd64.whl.metadata (541 bytes)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Collecting rich<14,>=10.14.0 (from streamlit)\n",
      "  Obtaining dependency information for rich<14,>=10.14.0 from https://files.pythonhosted.org/packages/87/67/a37f6214d0e9fe57f6ae54b2956d550ca8365857f42a1ce0392bb21d9410/rich-13.7.1-py3-none-any.whl.metadata\n",
      "  Downloading rich-13.7.1-py3-none-any.whl.metadata (18 kB)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (4.7.1)\n",
      "Collecting tzlocal<6,>=1.1 (from streamlit)\n",
      "  Obtaining dependency information for tzlocal<6,>=1.1 from https://files.pythonhosted.org/packages/97/3f/c4c51c55ff8487f2e6d0e618dba917e3c3ee2caae6cf0fbb59c9b1876f2e/tzlocal-5.2-py3-none-any.whl.metadata\n",
      "  Downloading tzlocal-5.2-py3-none-any.whl.metadata (7.8 kB)\n",
      "Collecting validators<1,>=0.2 (from streamlit)\n",
      "  Obtaining dependency information for validators<1,>=0.2 from https://files.pythonhosted.org/packages/3a/0c/785d317eea99c3739821718f118c70537639aa43f96bfa1d83a71f68eaf6/validators-0.22.0-py3-none-any.whl.metadata\n",
      "  Downloading validators-0.22.0-py3-none-any.whl.metadata (4.7 kB)\n",
      "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
      "  Obtaining dependency information for gitpython!=3.1.19,<4,>=3.0.7 from https://files.pythonhosted.org/packages/67/c7/995360c87dd74e27539ccbfecddfb58e08f140d849fcd7f35d2ed1a5f80f/GitPython-3.1.42-py3-none-any.whl.metadata\n",
      "  Downloading GitPython-3.1.42-py3-none-any.whl.metadata (12 kB)\n",
      "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
      "  Obtaining dependency information for pydeck<1,>=0.8.0b4 from https://files.pythonhosted.org/packages/10/4b/2fc80540e2d3903452245bb657c7f758ec7342420507d1e4091b0161856e/pydeck-0.8.1b0-py2.py3-none-any.whl.metadata\n",
      "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl.metadata (3.9 kB)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: toolz in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Obtaining dependency information for gitdb<5,>=4.0.1 from https://files.pythonhosted.org/packages/fd/5b/8f0c4a5bb9fd491c277c21eff7ccae71b47d43c4446c9d0c6cff2fe8c2c4/gitdb-4.0.11-py3-none-any.whl.metadata\n",
      "  Downloading gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from importlib-metadata<8,>=1.4->streamlit) (3.11.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Obtaining dependency information for smmap<6,>=3.0.1 from https://files.pythonhosted.org/packages/a7/a5/10f97f73544edcdef54409f1d839f6049a0d79df68adbc1ceb24d1aaca42/smmap-5.0.1-py3-none-any.whl.metadata\n",
      "  Downloading smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\pedro.seixas\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Downloading streamlit-1.31.1-py2.py3-none-any.whl (8.4 MB)\n",
      "   ---------------------------------------- 0.0/8.4 MB ? eta -:--:--\n",
      "    --------------------------------------- 0.2/8.4 MB 3.5 MB/s eta 0:00:03\n",
      "   -- ------------------------------------- 0.5/8.4 MB 5.6 MB/s eta 0:00:02\n",
      "   ------ --------------------------------- 1.3/8.4 MB 10.0 MB/s eta 0:00:01\n",
      "   ------------- -------------------------- 2.8/8.4 MB 14.8 MB/s eta 0:00:01\n",
      "   ---------------------- ----------------- 4.6/8.4 MB 19.6 MB/s eta 0:00:01\n",
      "   ------------------------------- -------- 6.6/8.4 MB 23.4 MB/s eta 0:00:01\n",
      "   -------------------------------------- - 8.2/8.4 MB 24.8 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 8.4/8.4 MB 23.3 MB/s eta 0:00:00\n",
      "Downloading altair-5.2.0-py3-none-any.whl (996 kB)\n",
      "   ---------------------------------------- 0.0/996.9 kB ? eta -:--:--\n",
      "   --------------------------------------- 996.9/996.9 kB 30.8 MB/s eta 0:00:00\n",
      "Downloading blinker-1.7.0-py3-none-any.whl (13 kB)\n",
      "Downloading cachetools-5.3.3-py3-none-any.whl (9.3 kB)\n",
      "Downloading GitPython-3.1.42-py3-none-any.whl (195 kB)\n",
      "   ---------------------------------------- 0.0/195.4 kB ? eta -:--:--\n",
      "   --------------------------------------- 195.4/195.4 kB 11.6 MB/s eta 0:00:00\n",
      "Downloading protobuf-4.25.3-cp310-abi3-win_amd64.whl (413 kB)\n",
      "   ---------------------------------------- 0.0/413.4 kB ? eta -:--:--\n",
      "   --------------------------------------- 413.4/413.4 kB 25.2 MB/s eta 0:00:00\n",
      "Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
      "   ---------------------------------------- 0.0/4.8 MB ? eta -:--:--\n",
      "   ---------------- ----------------------- 2.0/4.8 MB 42.7 MB/s eta 0:00:01\n",
      "   --------------------------------- ------ 4.0/4.8 MB 42.5 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 4.5/4.8 MB 41.1 MB/s eta 0:00:01\n",
      "   ---------------------------------------  4.8/4.8 MB 27.8 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 4.8/4.8 MB 23.6 MB/s eta 0:00:00\n",
      "Downloading rich-13.7.1-py3-none-any.whl (240 kB)\n",
      "   ---------------------------------------- 0.0/240.7 kB ? eta -:--:--\n",
      "   ---------------------------------------- 240.7/240.7 kB ? eta 0:00:00\n",
      "Downloading tzlocal-5.2-py3-none-any.whl (17 kB)\n",
      "Downloading validators-0.22.0-py3-none-any.whl (26 kB)\n",
      "Downloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
      "   ---------------------------------------- 0.0/62.7 kB ? eta -:--:--\n",
      "   ---------------------------------------- 62.7/62.7 kB ? eta 0:00:00\n",
      "Downloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
      "Installing collected packages: validators, tzlocal, smmap, protobuf, cachetools, blinker, rich, pydeck, gitdb, gitpython, altair, streamlit\n",
      "Successfully installed altair-5.2.0 blinker-1.7.0 cachetools-5.3.3 gitdb-4.0.11 gitpython-3.1.42 protobuf-4.25.3 pydeck-0.8.1b0 rich-13.7.1 smmap-5.0.1 streamlit-1.31.1 tzlocal-5.2 validators-0.22.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "237e6fd2-bd0e-4215-b72a-af827f65cbd0",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1b9033a0-3034-4d83-af8b-f7f2dd2124ca",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-03-04 20:42:17.137 No runtime found, using MemoryCacheStorageManager\n"
     ]
    }
   ],
   "source": [
    "st.set_page_config(page_title=\"O site do time mais brabo de tecnologia!\")\n",
    "\n",
    "with st.container():\n",
    "    st.title(\"Participantes do time mais brabo de tecnologia\")\n",
    "    st.image(\"logo vitrine.jpg\", caption=\"Logo mais bonito de todos os e-commereces de todas as galáxias\")\n",
    "    st.write(\"Informações dos brabos do time tech\")\n",
    "    \n",
    "\n",
    "@st.cache_data\n",
    "def carregar_tabela():\n",
    "    tabela = pd.read_csv(\"tabela.csv\")\n",
    "    return tabela\n",
    "\n",
    "with st.container():\n",
    "    st.write(carregar_tabela)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "84450271-1ba4-4171-b52b-9d30feb19ee5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-03-04 20:42:22.631 No runtime found, using MemoryCacheStorageManager\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Cargo</th>\n",
       "      <th>Equipe</th>\n",
       "      <th>Nome</th>\n",
       "      <th>Sobrenome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Gestor</td>\n",
       "      <td>Tecnologia</td>\n",
       "      <td>Eliseu</td>\n",
       "      <td>Santos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Assistente</td>\n",
       "      <td>Tecnologia</td>\n",
       "      <td>Pedro</td>\n",
       "      <td>Lima</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Cargo      Equipe    Nome Sobrenome\n",
       "0      Gestor  Tecnologia  Eliseu    Santos\n",
       "1  Assistente  Tecnologia   Pedro      Lima"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "carregar_tabela()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8f6b094-a199-4ae8-9b6d-38acb2a33952",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
