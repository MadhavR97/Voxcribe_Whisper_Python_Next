# Voxscribe Frontend Setup Guide

This guide explains how to set up and run the Voxscribe frontend after cloning the repository.

## Prerequisites

- Node.js 18+
- npm or yarn package manager

## Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/MadhavR97/Voxcribe_Python_Whisper_Frontend.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd Voxcribe_Python_Whisper_Frontend
   ```

3. **Install dependencies**
   ```bash
   npm install
   ```
   or
   ```bash
   yarn install
   ```

4. **Create environment file**
   ```bash
   cp .env.example .env.local
   ```
   
   Edit `.env.local` to point to your backend URL if needed. By default it's set to `BACKEND_URL=http://localhost:8000`.

5. **Run the development server**
   ```bash
   npm run dev
   ```
   or
   ```bash
   yarn dev
   ```

6. **Access the application**
   Open your browser and go to `http://localhost:3000`

## Notes

- Make sure the backend service is running before starting the frontend
- The frontend expects the backend to be available at the URL specified in the `BACKEND_URL` environment variable
- For production deployments, update the `BACKEND_URL` accordingly