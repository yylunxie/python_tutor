# 第二週：進階圖形處理與事件響應

繼上周對Pygame的基本介紹和簡單應用之後，本週我們將進一步深入學習Pygame的圖形處理和事件響應能力。我們將探討如何使用Pygame加載和處理圖片，實現複雜的圖形繪製，以及如何處理更多種類的用戶輸入事件。

## 複習上週內容

上週，我們學習了如何安裝Pygame，創建第一個Pygame窗口，並進行了基本的繪圖操作。我們也介紹了幾個重要的Pygame方法，包括：

- `pygame.init()`
- `pygame.display.set_mode(size)`
- `pygame.display.set_caption(title)`
- `pygame.event.get()`
- `pygame.draw.circle(surface, color, center, radius)`
- `pygame.display.flip()`
- `pygame.display.update()`

## 本週學習目標

- **進階圖形繪製**：學習如何繪製更複雜的圖形，包括線條、矩形、多邊形等。
- **圖片處理**：學習如何在Pygame中加載和顯示圖片，以及如何對圖片進行基本處理。
- **進階事件處理**：探討如何處理更多種類的事件，包括鍵盤按鍵事件和滑鼠事件。

## 進階圖形繪製

在Pygame中，除了圓形，我們還可以使用以下方法繪製其他類型的圖形：

- **繪製線條**：
    
    ```python
    pygame.draw.line(screen, color, start_pos, end_pos, width)
    ```
    
- **繪製矩形**：
    
    ```python
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    ```
    
- **繪製多邊形**：
    
    ```python
    pygame.draw.polygon(screen, color, points)
    ```
    

## 圖片處理

加載和顯示圖片是遊戲開發中的一個常見需求。Pygame提供了簡單的方法來加載圖片並將其繪製到螢幕上：

```python
image = pygame.image.load('path/to/image.png').convert()
screen.blit(image, (x, y))
```

## **進階事件處理**

為了使遊戲互動更加豐富，我們需要處理更多種類的事件：

- **鍵盤事件**：
    
    ```python
    pythonCopy code
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            # 處理向左移動
    ```
    
- **滑鼠事件**：
    
    ```python
    pythonCopy code
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            # 處理滑鼠左鍵點擊
    ```
    

## **本週挑戰**

利用本週學到的知識，嘗試製作一個簡單的遊戲原型，其中包含角色移動和基本的互動元素。使用進階圖形繪製技巧來美化遊戲場景，並加入圖片元素增加遊戲的視覺吸引力。

### **課堂練習：動態圖形繪製**

**目標**：讓學生們通過繪製一系列動態圖形，來理解Pygame的事件處理和圖形繪製方法。

**題目描述**：

- 創建一個Pygame窗口，窗口背景為黑色。
- 使用鍵盤上下左右鍵，控制一個矩形在窗口內移動。
- 矩形每移動到窗口的邊緣，自動改變顏色（顏色隨機生成）。

**提示**：

1. 使用 **`pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))`** 繪製矩形。
2. 監聽 **`KEYDOWN`** 事件，並根據按鍵（**`K_LEFT`**, **`K_RIGHT`**, **`K_UP`**, **`K_DOWN`**）更新矩形的位置。
3. 使用 **`randint`** 從 **`random`** 模塊生成隨機顏色。

### **回家作業：簡單的圖片處理遊戲**

**目標**：讓學生利用學到的圖片處理技術，製作一個簡單的遊戲或互動程序。

**作業要求**：

- 創建一個Pygame窗口，加載並顯示一張圖片。
- 當用戶點擊圖片時，圖片會移動到窗口中的一個隨機位置。
- 每當圖片移動時，窗口背景顏色也隨機改變。

**進階要求**（可選）：

- 增加一個計數器，記錄用戶點擊圖片的次數，並在窗口的某個位置顯示計數器的值。
- 當用戶點擊圖片超過10次後，顯示一條恭喜消息，並結束遊戲。

**提示**：

1. 使用 **`pygame.image.load()`** 加載圖片，並使用 **`screen.blit()`** 在指定位置顯示。
2. 監聽 **`MOUSEBUTTONDOWN`** 事件，並檢查點擊位置是否在圖片範圍內。
3. 使用 **`random`** 模塊的 **`randint`** 函數來生成隨機背景顏色和圖片的新位置。