你可以先克隆空的仓库，再新建并上传分支。步骤如下：

1. 克隆空的仓库（不下载所有内容）：   
   ```bash
   git clone --no-checkout https://gitlab.com/你的仓库名.git
   cd 你的仓库名
   ```

2. 创建一个新的分支：
   ```bash
   git checkout --orphan 新分支名
   ```

3. 添加你的文件并提交：
   ```bash
   git add .
   git commit -m "初始化提交"
   ```

4. 推送新分支到远程仓库：
   ```bash
   git push origin 新分支名
   ```
