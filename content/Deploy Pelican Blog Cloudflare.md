Title: Deploy Pelican Blog on Cloudflare
Date: 2023-08-28
Category: Blog

**I have made some blog posts and generated the staic files with pelican, which works locally. I have purchased a domain on cloudflare, now how do I publish/deploy my blog to it?**

To deploy your static website generated with Pelican to a domain purchased through Cloudflare, you would typically use a web hosting service that supports static websites. Cloudflare itself does not host websites, but they provide a DNS service, among other things. One popular choice for hosting static websites is Cloudflare Pages or GitHub Pages. Here's a step-by-step guide using Cloudflare Pages:

## Deploying a Pelican Blog using Cloudflare Pages

1. **GitHub Repository**: If you haven't already, push your Pelican website's source files (not the generated content) to a GitHub repository.

2. **Sign in to Cloudflare**: Log into your Cloudflare account and navigate to the "Pages" section.

3. **Create a New Project**: Click on "Create a project". Select the GitHub repository you just pushed your Pelican website to.

4. **Configure the Build Settings**: 
   - In the "Build Settings" section, set the build command to how you typically generate your Pelican static content. This is typically `pelican content` for default setups.
   - Set the "Build Output Directory" to the directory where Pelican outputs your static website. This is usually `output/`.

5. **Deploy**: Click "Begin setup", and Cloudflare Pages will deploy your site. 

6. **Custom Domain**: 
   - Once deployed, you can go to the "Settings" of your Cloudflare Pages project and navigate to the "Custom domains" section.
   - Here you can add your purchased domain. Cloudflare will guide you on updating DNS settings if needed.

7. **Update DNS Settings**:
   - Go to the DNS section in your Cloudflare dashboard.
   - Add a CNAME record pointing your domain to your `<username>.pages.dev`, where `<username>` is your Cloudflare username or the name given to your Cloudflare Pages project.

8. **Wait for Propagation**: DNS changes might take some time to propagate, ranging from a few minutes to 48 hours. Once propagated, visiting your domain should display your Pelican blog.

9. **Activate HTTPS**: Cloudflare usually auto-configures SSL for you, but you can go to the SSL/TLS section of your Cloudflare dashboard to adjust settings if necessary.

10. **Continuous Deployment**: One of the benefits of using Cloudflare Pages is that every time you push changes to your GitHub repository, Cloudflare will automatically rebuild and redeploy your site.

That's it! Your Pelican blog is now hosted with Cloudflare Pages and accessible through your custom domain.

**About pushing the source files, can you be more specific which files this is? Is it the pelicanconf.py, publishconf.py and the markdown files in the content folder?**

Yes, when referring to the "source files" of your Pelican website, it generally pertains to the set of files that are essential to regenerate the static content of your site. This typically includes:

1. **`pelicanconf.py`**: This is your main Pelican configuration file which holds settings and configurations for your site.

2. **`publishconf.py`**: If you have this file, it usually contains settings that are specifically for the production version of your site. 

3. **`content/` directory**: This folder contains all your blog posts, pages, and other content written in Markdown, reStructuredText, or other formats supported by Pelican. It's essential because without it, there would be no content to generate the static site from.

4. **`themes/` directory (if you have a custom theme)**: If you've made a custom theme or have downloaded and made changes to an existing one, this folder will hold all the necessary templates and static files for your theme.

5. **`plugins/` directory (if you use any)**: Some Pelican sites use plugins to extend functionality. If you've added any plugins to your site, they are typically stored here.

6. **Any other configuration or asset files**: This could include files like `requirements.txt` if you're tracking Python dependencies or any other asset or configuration files that your site relies on.

When you push these files to a repository, the idea is that anyone (or any service, like Cloudflare Pages) can clone your repository, run Pelican with your configuration, and produce an identical static website. 

However, you typically don't want to include the generated `output/` directory in this repository since that's the generated content and can be recreated from the source files. If you've already generated this and don't want to include it in the repository, you can add `output/` to a `.gitignore` file.

**I tried to begin setup, but I got this error: 13:38:34.601 Cloning repository... 13:38:35.469 From https://github.com/fredrikskatland/pelican-test 13:38:35.470 * branch 93a68d4d74ac94168727159c432ce507f54e768a -> FETCH_HEAD 13:38:35.470 13:38:35.524 HEAD is now at 93a68d4 Initial commit 13:38:35.524 13:38:35.631 13:38:35.663 Success: Finished cloning repository files 13:38:36.342 Detected the following tools from environment: 13:38:36.343 Executing user command: pelican content 13:38:36.353 /bin/sh: 1: pelican: not found 13:38:36.354 Failed: Error while executing user command. Exited with error code: 127 13:38:36.362 Failed: build command exited with code: 1 13:38:37.200 Failed: error occurred while running build command**

The error you're facing is due to the fact that the Cloudflare Pages build environment does not have `pelican` pre-installed. As a result, when it tries to execute the `pelican content` command, it can't find the `pelican` tool.

To resolve this, you need to:

1. **Include a `requirements.txt` file in your repository**: This file should list all the Python packages required for your blog. At a minimum, it should have `pelican` and any other plugins or dependencies you're using.

   ```plaintext
   pelican==<your-version>
   some-plugin==<version>
   ...
   ```

2. **Update your build command**: Modify your build command to first install the required packages and then generate the static content.

   ```bash
   pip install -r requirements.txt && pelican content
   ```

Here's a step-by-step guide to help you set this up:

1. **Create a `requirements.txt` file** in the root of your repository.

2. Add the necessary dependencies to this file. As mentioned above, at the very least, you'll want to include `pelican` and any other plugins or dependencies your blog requires.

3. Commit and push this `requirements.txt` file to your GitHub repository.

4. In Cloudflare Pages, update your build command to the one mentioned above: `pip install -r requirements.txt && pelican content`

5. Save your settings and try deploying again.

This should ensure that the required dependencies are installed before the build command is executed, allowing `pelican` and any other necessary tools to be available during the build process.

[[Getting started with Pelican]]
[[Pelican Pros, Cons, Tips]]
[[Domain registrars and DNS]]
[[Static site generators]]
[[Chat om domene og blogg]]
