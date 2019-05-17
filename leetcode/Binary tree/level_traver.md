因为在写最小深度用层次遍历时候写过，代码如下

        res = []
        if not root :
            return res
        q = [root]
        while q:
            for i in range(len(q)):
                r=q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                res.append(r.val)
        return res

但是，在leetcode上运行时候发现它的输出有个嵌套队列，于是代码加个s队列

        res = []
        if not root:
            return res
        q = [root]
        while q:
            s = []
            for i in range(len(q)):
                r=q.pop(0)
                s.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            res.append(s)
        return res