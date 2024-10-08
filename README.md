# pytorch
딥러닝을 위한 파이토치 입문

```
ssh-keygen -t rsa -b 4096 -C choyoon8282@gmail.com -f ~/.ssh/choyoon8282-github-key
ssh-keygen -t rsa -b 4096 -C choyoon8282@gmail.com -f C:/Users/hungh/.ssh/choyoon8282-github-key (파워쉘)
git bash (안해도 될것 같...)
cd .ssh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/choyoon8282-github-key
깃허브 - 셋팅 - ssh키 등록
파워쉘에서 
cd 소스코드위치
git remote set-url origin git@github.com:choyoon82/pytorch.git    # ssh 로 접속하도록 함. 
git config --local core.sshCommand "ssh -i ~/.ssh/choyoon8282-github-key"  # 강제로 해당 키를 쓰도록 함. 
ssh -T git@github.com  # 접속 테스트 
```
