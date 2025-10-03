# Testing Your Deployment - Complete Guide

## 🔍 Testing Methods

### 1. **GitHub Actions Testing**

#### Test the Workflow
```bash
# Method 1: Push a small change to trigger deployment
echo "# Test deployment - $(date)" >> README.md
git add README.md
git commit -m "Test deployment trigger"
git push origin mkdocs-enabled-submodules-added
```

#### Monitor the Actions
1. Go to your GitHub repository
2. Click **Actions** tab
3. Watch the "Deploy MkDocs to AWS EC2" workflow
4. Check each step for success/failure

#### Check Logs
- Click on the running/completed workflow
- Expand each step to see detailed logs
- Look for:
  - ✅ Submodule cloning success
  - ✅ MkDocs build completion
  - ✅ File transfer to EC2
  - ❌ Any error messages

### 2. **Local Testing (Before Deployment)**

#### Test MkDocs Build Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Test build locally
mkdocs build

# Test serve locally
mkdocs serve
# Then visit: http://127.0.0.1:8000
```

#### Test Submodule Access
```bash
# Test if submodules can be cloned
git submodule update --init --recursive

# Check if BMS docs exist
ls -la simtestlab/bms_software/docs/
```

### 3. **EC2 Server Testing**

#### SSH into Your EC2 Instance
```bash
# Replace with your actual values
ssh -i your-key.pem ubuntu@your-ec2-ip
```

#### Check Deployment Status (Run on EC2)
```bash
# Use the status check script
chmod +x /home/ubuntu/check-deployment.sh
./check-deployment.sh

# Or manual checks:
sudo systemctl status nginx
ls -la /var/www/simtestlab/
curl -I localhost
```

#### Check Site Files (Run on EC2)
```bash
# Check if files were deployed
ls -la /var/www/simtestlab/

# Check recent file modifications
find /var/www/simtestlab -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort -r | head -10

# Check if BMS documentation exists
ls -la /var/www/simtestlab/bms_software/

# Test site response
curl -v http://localhost/
```

### 4. **Web Browser Testing**

#### Direct IP Access
```bash
# Visit your EC2 public IP directly
http://YOUR-EC2-PUBLIC-IP
```

#### Domain Testing (if configured)
```bash
# Visit your domain
http://your-domain.com
https://your-domain.com  # if SSL is configured
```

#### Test Specific Pages
- Main page: `http://your-site/`
- BMS docs: `http://your-site/bms_software/`
- Blog: `http://your-site/blog/`
- Search functionality
- Navigation links

### 5. **Automated Testing Script**

Let me create a test script for you: