# security-architecture
Security Architecture Demo

# 🚨 Security Architecture Demo - INSECURE BY DESIGN

**WARNING:** This repository is intentionally insecure for educational purposes!

## 🎯 Workshop Exercise: Secure This Repo!

Your mission: This repository has **terrible security practices**. Work with your team to fix them using GitHub's built-in security features!

---

## 📋 Team Exercise Checklist

### Phase 1: Discovery (5 minutes)
🔍 **Hunt for security issues in this repo:**
- [ ] Find exposed secrets (API keys, passwords)
- [ ] Identify sensitive data that shouldn't be committed
- [ ] Check for vulnerable dependencies
- [ ] Look for missing security controls

### Phase 2: Secure It! (20 minutes)

#### Step 1: Create .gitignore
- [ ] Create a `.gitignore` file in the root directory
- [ ] Add these entries:
  ```
  .env
  *.csv
  *key*.txt
  config.py
  __pycache__/
  node_modules/
  ```

#### Step 2: Move Secrets to Environment Variables
- [ ] Create `.env.example` with dummy values
- [ ] Remove real secrets from `.env` (which is now ignored)
- [ ] Update `config.py` to read from environment variables

#### Step 3: Enable GitHub Security Features
- [ ] Go to **Settings → Security → Code security and analysis**
- [ ] Enable **Dependency alerts** (Dependabot)
- [ ] Enable **Secret scanning**
- [ ] Enable **Dependabot security updates**

#### Step 4: Set Up Branch Protection
- [ ] Go to **Settings → Branches → Add branch protection rule**
- [ ] Branch name: `main`
- [ ] Enable: "Require pull request before merging"
- [ ] Enable: "Require status checks before merging"

#### Step 5: Fix Dependencies
- [ ] Review Dependabot alerts (should appear in ~5 minutes)
- [ ] Update `requirements.txt` to latest secure versions
- [ ] Update `package.json` to latest secure versions

#### Step 6: Clean Up Sensitive Files
- [ ] Delete `user_data.csv` from the repository
- [ ] Delete `api_keys.txt` from the repository
- [ ] Commit the deletions

---

## 🏆 Bonus Challenges

- [ ] Find how many CVEs (vulnerabilities) Dependabot reports
- [ ] Remove sensitive data from Git history using `git filter-branch`
- [ ] Add a `SECURITY.md` file with responsible disclosure policy
- [ ] Create a pull request template

---

## 💡 What You're Learning

- **Defense in Depth**: Multiple layers of security (just like the Tower of London!)
- **Secrets Management**: Never commit credentials
- **Dependency Security**: Keep packages up to date
- **Access Control**: Branch protection prevents direct pushes
- **Automation**: GitHub security features catch issues automatically

---

## 🎓 Discussion Questions

1. What would happen if these secrets were in a real, public repository?
2. How quickly could Dependabot have prevented a security incident?
3. Why is branch protection important for team projects?
4. What other security practices should be part of every project?

---

**Remember:** This is a learning exercise. Never commit real secrets to any repository!
