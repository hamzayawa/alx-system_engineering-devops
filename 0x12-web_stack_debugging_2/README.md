# 0x12. Web Stack Debugging #2

![Debug](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/eaeff07a715ff880b1ceb8e863a1d141a74a7f85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230718%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230718T024646Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=43eb824aa1011a6e0f05096985a5d32ce52925baff430093153b34a0b0536f73)

The user `root` is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run `rm -rf /`, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the `root` user can do, just need to use a specific command that you need to discover.

For the containers that you are given in this project as well as the checker, everything is run under the `root` user, which has the ability to run anything as another user.
