import cv2
import os


def detect_shapes():

    os.makedirs(r'C:\Users\fajra\PycharmProjects\Task2\assets\output_results', exist_ok=True)


    img = cv2.imread(r'C:\Users\fajra\PycharmProjects\Task2\assets\input_images\Shapes.jpg')
    if img is None:
        print("image not found")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    counts = {"Triangle": 0, "Square": 0, "Rectangle": 0, "Circle": 0}
    img_area = img.shape[0] * img.shape[1]

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 500 or area > (img_area * 0.9):
            continue


        epsilon = 0.035 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        vertices = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h

        label = ""
        if vertices == 3:
            label = "Triangle"
        elif vertices == 4:
            if 0.85 <= aspect_ratio <= 1.15:
                label = "Square"
            else:
                label = "Rectangle"
        elif vertices >= 7:
            label = "Circle"

        if label != "":
            counts[label] += 1
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
            cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)


    print("\n--- Results ---")
    for shape, count in counts.items():
        print(f"{shape}: {count}")


    cv2.imwrite(r'C:\Users\fajra\PycharmProjects\Task2\assets\output_results\final_result.jpg', img)
    print("\nSaved successfully in assets/output_results/final_result.jpg")


    cv2.imshow('Final Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_shapes()