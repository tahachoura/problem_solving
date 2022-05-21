```
# Problem:
![image](https://user-images.githubusercontent.com/11164303/169665991-5ef6b618-265f-4fcb-bdb4-bbe58f04b582.png)


-------- 
# Solution:
```


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current and current.next:
            if current.val==current.next.val: current.next=current.next.next
            else: current=current.next
        return head
