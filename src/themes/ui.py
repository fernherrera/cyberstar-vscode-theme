from dataclasses import dataclass
from typing import Optional

from .base_theme import Theme


@dataclass
class UI:
    """Creates a UI configuration object based on the provided theme and optional parameters

    @param theme: The theme object
    @returns: A partial VSCodeThemeColors object representing the UI configuration.
    """

    theme: Theme = Theme()

    def __init__(self, theme: Theme):
        """_summary_

        Args:
            theme (Theme): _description_
        """
        self.theme = theme

    def build(self):
        return {
            **self.activityBarColors(),
            **self.badgeColors(),
            **self.bannerColors(),
            **self.breadcrumbColors(),
            **self.buttonColors(),
            **self.chartColors(),
            **self.chatColors(),
            **self.checkboxColors(),
            **self.commandCenterColors(),
            **self.commentsViewColors(),
            **self.contrastColors(),
            **self.debugColors(),
            **self.descriptionColors(),
            **self.diffEditorColors(),
            **self.disabledColors(),
            **self.dropdownColors(),
            **self.editorColors(),
            **self.errorColors(),
            **self.extensionColors(),
            **self.gaugeColors(),
            **self.generalColors(),
            **self.gitColors(),
            **self.inlineColors(),
            **self.inputColors(),
            **self.inputOptionColors(),
            **self.inputValidationColors(),
            **self.interactiveColors(),
            **self.issuesColors(),
            **self.keyBindingColors(),
            **self.listColors(),
            **self.menuColors(),
            **self.mergeColors(),
            **self.minimapColors(),
            **self.multiDiffEditorColors(),
            **self.notebookColors(),
            **self.notificationsColors(),
            **self.outputViewColors(),
            **self.panelColors(),
            **self.peekViewColors(),
            **self.pickerGroupColors(),
            **self.portsColors(),
            **self.problemsColors(),
            **self.profileColors(),
            **self.progressBarColors(),
            **self.pullRequestsColors(),
            **self.quickInputColors(),
            **self.radioColors(),
            **self.sashColors(),
            **self.scmGraphColors(),
            **self.scrollBarColors(),
            **self.searchColors(),
            **self.selectionColors(),
            **self.settingsColors(),
            **self.sideBarColors(),
            **self.statusBarColors(),
            **self.symbolIconsColors(),
            **self.tabColors(),
            **self.terminalColors(),
            **self.testingColors(),
            **self.textColors(),
            **self.titleBarColors(),
            **self.toolbarColors(),
            **self.treeColors(),
            **self.walkThroughColors(),
            **self.welcomePageColors(),
            **self.widgetColors(),
            **self.windowColors(),
        }

    def activityBarColors(self):
        return {
            "actionBar.toggledBackground": "#000000",
            "activityBar.activeBackground": "#000000",
            "activityBar.activeBorder": "#000000",
            "activityBar.activeFocusBorder": "#000000",
            "activityBar.background": "#000000",
            "activityBar.border": "#000000",
            "activityBar.dropBorder": "#000000",
            "activityBar.foreground": self.theme.foreground,
            "activityBar.inactiveForeground": self.theme.foreground_darker,
            "activityBarBadge.background": "#000000",
            "activityBarBadge.foreground": self.theme.foreground,
            "activityBarTop.activeBackground": "#000000",
            "activityBarTop.activeBorder": "#000000",
            "activityBarTop.background": "#000000",
            "activityBarTop.dropBorder": "#000000",
            "activityBarTop.foreground": self.theme.foreground,
            "activityBarTop.inactiveForeground": self.theme.foreground_darker,
            "activityErrorBadge.background": "#000000",
            "activityErrorBadge.foreground": self.theme.foreground,
            "activityWarningBadge.background": "#000000",
            "activityWarningBadge.foreground": self.theme.foreground,
        }

    def badgeColors(self):
        return {
            "badge.background": self.theme.background,
            "badge.foreground": self.theme.foreground,
        }

    def bannerColors(self):
        return {
            "banner.background": self.theme.background,
            "banner.foreground": self.theme.foreground,
            "banner.iconForeground": self.theme.foreground,
        }

    def breadcrumbColors(self):
        return {
            "breadcrumb.activeSelectionForeground": "#000000",
            "breadcrumb.background": "#000000",
            "breadcrumb.focusForeground": "#000000",
            "breadcrumb.foreground": "#000000",
            "breadcrumbPicker.background": "#000000",
        }

    def buttonColors(self):
        return {
            "button.background": "#000000",
            "button.border": "#000000",
            "button.foreground": "#000000",
            "button.hoverBackground": "#000000",
            "button.secondaryBackground": "#000000",
            "button.secondaryForeground": "#000000",
            "button.secondaryHoverBackground": "#000000",
            "button.separator": "#000000",
        }

    def chartColors(self):
        return {
            "chart.axis": "#000000",
            "chart.guide": "#000000",
            "chart.line": "#000000",
            "charts.blue": "#000000",
            "charts.foreground": "#000000",
            "charts.green": "#000000",
            "charts.lines": "#000000",
            "charts.orange": "#000000",
            "charts.purple": "#000000",
            "charts.red": "#000000",
            "charts.yellow": "#000000",
        }

    def chatColors(self):
        return {
            "chat.avatarBackground": "#000000",
            "chat.avatarForeground": "#000000",
            "chat.editedFileForeground": "#000000",
            "chat.requestBackground": "#000000",
            "chat.requestBorder": "#000000",
            "chat.slashCommandBackground": "#000000",
            "chat.slashCommandForeground": "#000000",
        }

    def checkboxColors(self):
        return {
            "checkbox.background": "#000000",
            "checkbox.border": "#000000",
            "checkbox.foreground": "#000000",
            "checkbox.selectBackground": "#000000",
            "checkbox.selectBorder": "#000000",
        }

    def commandCenterColors(self):
        return {
            "commandCenter.activeBackground": "#000000",
            "commandCenter.activeBorder": "#000000",
            "commandCenter.activeForeground": "#000000",
            "commandCenter.background": "#000000",
            "commandCenter.border": "#000000",
            "commandCenter.debuggingBackground": "#000000",
            "commandCenter.foreground": "#000000",
            "commandCenter.inactiveBorder": "#000000",
            "commandCenter.inactiveForeground": "#000000",
        }

    def commentsViewColors(self):
        return {
            "commentsView.resolvedIcon": "#000000",
            "commentsView.unresolvedIcon": "#000000",
        }

    def contrastColors(self):
        return {
            "contrastActiveBorder": "#000000",
            "contrastBorder": "#000000",
        }

    def debugColors(self):
        return {
            "debugConsole.errorForeground": "#000000",
            "debugConsole.infoForeground": "#000000",
            "debugConsole.sourceForeground": "#000000",
            "debugConsole.warningForeground": "#000000",
            "debugConsoleInputIcon.foreground": "#000000",
            "debugExceptionWidget.background": "#000000",
            "debugExceptionWidget.border": "#000000",
            "debugIcon.breakpointCurrentStackframeForeground": "#000000",
            "debugIcon.breakpointDisabledForeground": "#000000",
            "debugIcon.breakpointForeground": "#000000",
            "debugIcon.breakpointStackframeForeground": "#000000",
            "debugIcon.breakpointUnverifiedForeground": "#000000",
            "debugIcon.continueForeground": "#000000",
            "debugIcon.disconnectForeground": "#000000",
            "debugIcon.pauseForeground": "#000000",
            "debugIcon.restartForeground": "#000000",
            "debugIcon.startForeground": "#000000",
            "debugIcon.stepBackForeground": "#000000",
            "debugIcon.stepIntoForeground": "#000000",
            "debugIcon.stepOutForeground": "#000000",
            "debugIcon.stepOverForeground": "#000000",
            "debugIcon.stopForeground": "#000000",
            "debugTokenExpression.boolean": "#000000",
            "debugTokenExpression.error": "#000000",
            "debugTokenExpression.name": "#000000",
            "debugTokenExpression.number": "#000000",
            "debugTokenExpression.string": "#000000",
            "debugTokenExpression.type": "#000000",
            "debugTokenExpression.value": "#000000",
            "debugToolBar.background": "#000000",
            "debugToolBar.border": "#000000",
            "debugView.exceptionLabelBackground": "#000000",
            "debugView.exceptionLabelForeground": "#000000",
            "debugView.stateLabelBackground": "#000000",
            "debugView.stateLabelForeground": "#000000",
            "debugView.valueChangedHighlight": "#000000",
        }

    def descriptionColors(self):
        return {"descriptionForeground": "#000000"}

    def diffEditorColors(self):
        return {
            "diffEditor.border": "#000000",
            "diffEditor.diagonalFill": "#000000",
            "diffEditor.insertedLineBackground": "#000000",
            "diffEditor.insertedTextBackground": "#000000",
            "diffEditor.insertedTextBorder": "#000000",
            "diffEditor.move.border": "#000000",
            "diffEditor.moveActive.border": "#000000",
            "diffEditor.removedLineBackground": "#000000",
            "diffEditor.removedTextBackground": "#000000",
            "diffEditor.removedTextBorder": "#000000",
            "diffEditor.unchangedCodeBackground": "#000000",
            "diffEditor.unchangedRegionBackground": "#000000",
            "diffEditor.unchangedRegionForeground": "#000000",
            "diffEditor.unchangedRegionShadow": "#000000",
            "diffEditorGutter.insertedLineBackground": "#000000",
            "diffEditorGutter.removedLineBackground": "#000000",
            "diffEditorOverview.insertedForeground": "#000000",
            "diffEditorOverview.removedForeground": "#000000",
        }

    def disabledColors(self):
        return {
            "disabledForeground": "#000000",
        }

    def dropdownColors(self):
        return {
            "dropdown.background": "#000000",
            "dropdown.border": "#000000",
            "dropdown.foreground": "#000000",
            "dropdown.listBackground": "#000000",
        }

    def editorColors(self):
        return {
            "editor.background": "#000000",
            "editor.compositionBorder": "#000000",
            "editor.findMatchBackground": "#000000",
            "editor.findMatchBorder": "#000000",
            "editor.findMatchForeground": "#000000",
            "editor.findMatchHighlightBackground": "#000000",
            "editor.findMatchHighlightBorder": "#000000",
            "editor.findMatchHighlightForeground": "#000000",
            "editor.findRangeHighlightBackground": "#000000",
            "editor.findRangeHighlightBorder": "#000000",
            "editor.focusedStackFrameHighlightBackground": "#000000",
            "editor.foldBackground": "#000000",
            "editor.foldPlaceholderForeground": "#000000",
            "editor.foreground": "#000000",
            "editor.hoverHighlightBackground": "#000000",
            "editor.inactiveSelectionBackground": "#000000",
            "editor.inlineValuesBackground": "#000000",
            "editor.inlineValuesForeground": "#000000",
            "editor.lineHighlightBackground": "#000000",
            "editor.lineHighlightBorder": "#000000",
            "editor.linkedEditingBackground": "#000000",
            "editor.placeholder.foreground": "#000000",
            "editor.rangeHighlightBackground": "#000000",
            "editor.rangeHighlightBorder": "#000000",
            "editor.selectionBackground": "#000000",
            "editor.selectionForeground": "#000000",
            "editor.selectionHighlightBackground": "#000000",
            "editor.selectionHighlightBorder": "#000000",
            "editor.snippetFinalTabstopHighlightBackground": "#000000",
            "editor.snippetFinalTabstopHighlightBorder": "#000000",
            "editor.snippetTabstopHighlightBackground": "#000000",
            "editor.snippetTabstopHighlightBorder": "#000000",
            "editor.stackFrameHighlightBackground": "#000000",
            "editor.symbolHighlightBackground": "#000000",
            "editor.symbolHighlightBorder": "#000000",
            "editor.wordHighlightBackground": "#000000",
            "editor.wordHighlightBorder": "#000000",
            "editor.wordHighlightStrongBackground": "#000000",
            "editor.wordHighlightStrongBorder": "#000000",
            "editor.wordHighlightTextBackground": "#000000",
            "editor.wordHighlightTextBorder": "#000000",
            "editorActionList.background": "#000000",
            "editorActionList.focusBackground": "#000000",
            "editorActionList.focusForeground": "#000000",
            "editorActionList.foreground": "#000000",
            "editorBracketHighlight.foreground1": "#000000",
            "editorBracketHighlight.foreground2": "#000000",
            "editorBracketHighlight.foreground3": "#000000",
            "editorBracketHighlight.foreground4": "#000000",
            "editorBracketHighlight.foreground5": "#000000",
            "editorBracketHighlight.foreground6": "#000000",
            "editorBracketHighlight.unexpectedBracket.foreground": "#000000",
            "editorBracketMatch.background": "#000000",
            "editorBracketMatch.border": "#000000",
            "editorBracketPairGuide.activeBackground1": "#000000",
            "editorBracketPairGuide.activeBackground2": "#000000",
            "editorBracketPairGuide.activeBackground3": "#000000",
            "editorBracketPairGuide.activeBackground4": "#000000",
            "editorBracketPairGuide.activeBackground5": "#000000",
            "editorBracketPairGuide.activeBackground6": "#000000",
            "editorBracketPairGuide.background1": "#000000",
            "editorBracketPairGuide.background2": "#000000",
            "editorBracketPairGuide.background3": "#000000",
            "editorBracketPairGuide.background4": "#000000",
            "editorBracketPairGuide.background5": "#000000",
            "editorBracketPairGuide.background6": "#000000",
            "editorCodeLens.foreground": "#000000",
            "editorCommentsWidget.rangeActiveBackground": "#000000",
            "editorCommentsWidget.rangeBackground": "#000000",
            "editorCommentsWidget.replyInputBackground": "#000000",
            "editorCommentsWidget.resolvedBorder": "#000000",
            "editorCommentsWidget.unresolvedBorder": "#000000",
            "editorCursor.background": "#000000",
            "editorCursor.foreground": "#000000",
            "editorError.background": "#000000",
            "editorError.border": "#000000",
            "editorError.foreground": "#000000",
            "editorGhostText.background": "#000000",
            "editorGhostText.border": "#000000",
            "editorGhostText.foreground": "#000000",
            "editorGroup.border": "#000000",
            "editorGroup.dropBackground": "#000000",
            "editorGroup.dropIntoPromptBackground": "#000000",
            "editorGroup.dropIntoPromptBorder": "#000000",
            "editorGroup.dropIntoPromptForeground": "#000000",
            "editorGroup.emptyBackground": "#000000",
            "editorGroup.focusedEmptyBorder": "#000000",
            "editorGroupHeader.border": "#000000",
            "editorGroupHeader.noTabsBackground": "#000000",
            "editorGroupHeader.tabsBackground": "#000000",
            "editorGroupHeader.tabsBorder": "#000000",
            "editorGutter.addedBackground": "#000000",
            "editorGutter.background": "#000000",
            "editorGutter.commentGlyphForeground": "#000000",
            "editorGutter.commentRangeForeground": "#000000",
            "editorGutter.commentUnresolvedGlyphForeground": "#000000",
            "editorGutter.deletedBackground": "#000000",
            "editorGutter.foldingControlForeground": "#000000",
            "editorGutter.itemBackground": "#000000",
            "editorGutter.itemGlyphForeground": "#000000",
            "editorGutter.modifiedBackground": "#000000",
            "editorHint.border": "#000000",
            "editorHint.foreground": "#000000",
            "editorHoverWidget.background": "#000000",
            "editorHoverWidget.border": "#000000",
            "editorHoverWidget.foreground": "#000000",
            "editorHoverWidget.highlightForeground": "#000000",
            "editorHoverWidget.statusBarBackground": "#000000",
            "editorIndentGuide.activeBackground1": "#000000",
            "editorIndentGuide.activeBackground2": "#000000",
            "editorIndentGuide.activeBackground3": "#000000",
            "editorIndentGuide.activeBackground4": "#000000",
            "editorIndentGuide.activeBackground5": "#000000",
            "editorIndentGuide.activeBackground6": "#000000",
            "editorIndentGuide.background1": "#000000",
            "editorIndentGuide.background2": "#000000",
            "editorIndentGuide.background3": "#000000",
            "editorIndentGuide.background4": "#000000",
            "editorIndentGuide.background5": "#000000",
            "editorIndentGuide.background6": "#000000",
            "editorInfo.background": "#000000",
            "editorInfo.border": "#000000",
            "editorInfo.foreground": "#000000",
            "editorInlayHint.background": "#000000",
            "editorInlayHint.foreground": "#000000",
            "editorInlayHint.parameterBackground": "#000000",
            "editorInlayHint.parameterForeground": "#000000",
            "editorInlayHint.typeBackground": "#000000",
            "editorInlayHint.typeForeground": "#000000",
            "editorLightBulb.foreground": "#000000",
            "editorLightBulbAi.foreground": "#000000",
            "editorLightBulbAutoFix.foreground": "#000000",
            "editorLineNumber.activeForeground": "#000000",
            "editorLineNumber.dimmedForeground": "#000000",
            "editorLineNumber.foreground": "#000000",
            "editorLink.activeForeground": "#000000",
            "editorMarkerNavigation.background": "#000000",
            "editorMarkerNavigationError.background": "#000000",
            "editorMarkerNavigationError.headerBackground": "#000000",
            "editorMarkerNavigationInfo.background": "#000000",
            "editorMarkerNavigationInfo.headerBackground": "#000000",
            "editorMarkerNavigationWarning.background": "#000000",
            "editorMarkerNavigationWarning.headerBackground": "#000000",
            "editorMinimap.inlineChatInserted": "#000000",
            "editorMultiCursor.primary.background": "#000000",
            "editorMultiCursor.primary.foreground": "#000000",
            "editorMultiCursor.secondary.background": "#000000",
            "editorMultiCursor.secondary.foreground": "#000000",
            "editorOverviewRuler.addedForeground": "#000000",
            "editorOverviewRuler.background": "#000000",
            "editorOverviewRuler.border": "#000000",
            "editorOverviewRuler.bracketMatchForeground": "#000000",
            "editorOverviewRuler.commentForeground": "#000000",
            "editorOverviewRuler.commentUnresolvedForeground": "#000000",
            "editorOverviewRuler.commonContentForeground": "#000000",
            "editorOverviewRuler.currentContentForeground": "#000000",
            "editorOverviewRuler.deletedForeground": "#000000",
            "editorOverviewRuler.errorForeground": "#000000",
            "editorOverviewRuler.findMatchForeground": "#000000",
            "editorOverviewRuler.incomingContentForeground": "#000000",
            "editorOverviewRuler.infoForeground": "#000000",
            "editorOverviewRuler.inlineChatInserted": "#000000",
            "editorOverviewRuler.inlineChatRemoved": "#000000",
            "editorOverviewRuler.modifiedForeground": "#000000",
            "editorOverviewRuler.rangeHighlightForeground": "#000000",
            "editorOverviewRuler.selectionHighlightForeground": "#000000",
            "editorOverviewRuler.warningForeground": "#000000",
            "editorOverviewRuler.wordHighlightForeground": "#000000",
            "editorOverviewRuler.wordHighlightStrongForeground": "#000000",
            "editorOverviewRuler.wordHighlightTextForeground": "#000000",
            "editorPane.background": "#000000",
            "editorRuler.foreground": "#000000",
            "editorStickyScroll.background": "#000000",
            "editorStickyScroll.border": "#000000",
            "editorStickyScroll.shadow": "#000000",
            "editorStickyScrollHover.background": "#000000",
            "editorSuggestWidget.background": "#000000",
            "editorSuggestWidget.border": "#000000",
            "editorSuggestWidget.focusHighlightForeground": "#000000",
            "editorSuggestWidget.foreground": "#000000",
            "editorSuggestWidget.highlightForeground": "#000000",
            "editorSuggestWidget.selectedBackground": "#000000",
            "editorSuggestWidget.selectedForeground": "#000000",
            "editorSuggestWidget.selectedIconForeground": "#000000",
            "editorSuggestWidgetStatus.foreground": "#000000",
            "editorUnicodeHighlight.background": "#000000",
            "editorUnicodeHighlight.border": "#000000",
            "editorUnnecessaryCode.border": "#000000",
            "editorUnnecessaryCode.opacity": "#000000",
            "editorWarning.background": "#000000",
            "editorWarning.border": "#000000",
            "editorWarning.foreground": "#000000",
            "editorWatermark.foreground": "#000000",
            "editorWhitespace.foreground": "#000000",
            "editorWidget.background": "#000000",
            "editorWidget.border": "#000000",
            "editorWidget.foreground": "#000000",
            "editorWidget.resizeBorder": "#000000",
        }

    def errorColors(self):
        return {
            "errorForeground": "#000000",
            "errorLens.errorBackground": "#000000",
            "errorLens.errorBackgroundLight": "#000000",
            "errorLens.errorForeground": "#000000",
            "errorLens.errorForegroundLight": "#000000",
            "errorLens.errorMessageBackground": "#000000",
            "errorLens.errorRangeBackground": "#000000",
            "errorLens.hintBackground": "#000000",
            "errorLens.hintBackgroundLight": "#000000",
            "errorLens.hintForeground": "#000000",
            "errorLens.hintForegroundLight": "#000000",
            "errorLens.hintMessageBackground": "#000000",
            "errorLens.hintRangeBackground": "#000000",
            "errorLens.infoBackground": "#000000",
            "errorLens.infoBackgroundLight": "#000000",
            "errorLens.infoForeground": "#000000",
            "errorLens.infoForegroundLight": "#000000",
            "errorLens.infoMessageBackground": "#000000",
            "errorLens.infoRangeBackground": "#000000",
            "errorLens.statusBarErrorForeground": "#000000",
            "errorLens.statusBarHintForeground": "#000000",
            "errorLens.statusBarIconErrorForeground": "#000000",
            "errorLens.statusBarIconWarningForeground": "#000000",
            "errorLens.statusBarInfoForeground": "#000000",
            "errorLens.statusBarWarningForeground": "#000000",
            "errorLens.warningBackground": "#000000",
            "errorLens.warningBackgroundLight": "#000000",
            "errorLens.warningForeground": "#000000",
            "errorLens.warningForegroundLight": "#000000",
            "errorLens.warningMessageBackground": "#000000",
            "errorLens.warningRangeBackground": "#000000",
        }

    def extensionColors(self):
        return {
            "extensionBadge.remoteBackground": "#000000",
            "extensionBadge.remoteForeground": "#000000",
            "extensionButton.background": "#000000",
            "extensionButton.foreground": "#000000",
            "extensionButton.hoverBackground": "#000000",
            "extensionButton.prominentBackground": "#000000",
            "extensionButton.prominentForeground": "#000000",
            "extensionButton.prominentHoverBackground": "#000000",
            "extensionButton.separator": "#000000",
            "extensionIcon.preReleaseForeground": "#000000",
            "extensionIcon.privateForeground": "#000000",
            "extensionIcon.sponsorForeground": "#000000",
            "extensionIcon.starForeground": "#000000",
            "extensionIcon.verifiedForeground": "#000000",
        }

    def gaugeColors(self):
        return {
            "gauge.background": "#000000",
            "gauge.border": "#000000",
            "gauge.errorBackground": "#000000",
            "gauge.errorForeground": "#000000",
            "gauge.foreground": "#000000",
            "gauge.warningBackground": "#000000",
            "gauge.warningForeground": "#000000",
        }

    def generalColors(self):
        return {
            "focusBorder": "#000000",
            "foreground": "#000000",
            "icon.foreground": "#000000",
        }

    def gitColors(self):
        return {
            "git.blame.editorDecorationForeground": "#000000",
            "gitDecoration.addedResourceForeground": "#000000",
            "gitDecoration.conflictingResourceForeground": "#000000",
            "gitDecoration.deletedResourceForeground": "#000000",
            "gitDecoration.ignoredResourceForeground": "#000000",
            "gitDecoration.modifiedResourceForeground": "#000000",
            "gitDecoration.renamedResourceForeground": "#000000",
            "gitDecoration.stageDeletedResourceForeground": "#000000",
            "gitDecoration.stageModifiedResourceForeground": "#000000",
            "gitDecoration.submoduleResourceForeground": "#000000",
            "gitDecoration.untrackedResourceForeground": "#000000",
        }

    def inlineColors(self):
        return {
            "inlineChat.background": "#000000",
            "inlineChat.border": "#000000",
            "inlineChat.foreground": "#000000",
            "inlineChat.shadow": "#000000",
            "inlineChatDiff.inserted": "#000000",
            "inlineChatDiff.removed": "#000000",
            "inlineChatInput.background": "#000000",
            "inlineChatInput.border": "#000000",
            "inlineChatInput.focusBorder": "#000000",
            "inlineChatInput.placeholderForeground": "#000000",
            "inlineEdit.gutterIndicator.background": "#000000",
            "inlineEdit.gutterIndicator.primaryBackground": "#000000",
            "inlineEdit.gutterIndicator.primaryBorder": "#000000",
            "inlineEdit.gutterIndicator.primaryForeground": "#000000",
            "inlineEdit.gutterIndicator.secondaryBackground": "#000000",
            "inlineEdit.gutterIndicator.secondaryBorder": "#000000",
            "inlineEdit.gutterIndicator.secondaryForeground": "#000000",
            "inlineEdit.gutterIndicator.successfulBackground": "#000000",
            "inlineEdit.gutterIndicator.successfulBorder": "#000000",
            "inlineEdit.gutterIndicator.successfulForeground": "#000000",
            "inlineEdit.modifiedBackground": "#000000",
            "inlineEdit.modifiedBorder": "#000000",
            "inlineEdit.modifiedChangedLineBackground": "#000000",
            "inlineEdit.modifiedChangedTextBackground": "#000000",
            "inlineEdit.originalBackground": "#000000",
            "inlineEdit.originalBorder": "#000000",
            "inlineEdit.originalChangedLineBackground": "#000000",
            "inlineEdit.originalChangedTextBackground": "#000000",
            "inlineEdit.tabWillAcceptModifiedBorder": "#000000",
            "inlineEdit.tabWillAcceptOriginalBorder": "#000000",
        }

    def inputColors(self):
        return {
            "input.background": "#000000",
            "input.border": "#000000",
            "input.foreground": "#000000",
            "input.placeholderForeground": "#000000",
        }

    def inputOptionColors(self):
        return {
            "inputOption.activeBackground": "#000000",
            "inputOption.activeBorder": "#000000",
            "inputOption.activeForeground": "#000000",
            "inputOption.hoverBackground": "#000000",
        }

    def inputValidationColors(self):
        return {
            "inputValidation.errorBackground": "#000000",
            "inputValidation.errorBorder": "#000000",
            "inputValidation.errorForeground": "#000000",
            "inputValidation.infoBackground": "#000000",
            "inputValidation.infoBorder": "#000000",
            "inputValidation.infoForeground": "#000000",
            "inputValidation.warningBackground": "#000000",
            "inputValidation.warningBorder": "#000000",
            "inputValidation.warningForeground": "#000000",
        }

    def interactiveColors(self):
        return {
            "interactive.activeCodeBorder": "#000000",
            "interactive.inactiveCodeBorder": "#000000",
        }

    def issuesColors(self):
        return {
            "issues.closed": "#000000",
            "issues.newIssueDecoration": "#000000",
            "issues.open": "#000000",
        }

    def keyBindingColors(self):
        return {
            "keybindingLabel.background": "#000000",
            "keybindingLabel.border": "#000000",
            "keybindingLabel.bottomBorder": "#000000",
            "keybindingLabel.foreground": "#000000",
            "keybindingTable.headerBackground": "#000000",
            "keybindingTable.rowsBackground": "#000000",
        }

    def listColors(self):
        return {
            "list.activeSelectionBackground": "#000000",
            "list.activeSelectionForeground": "#000000",
            "list.activeSelectionIconForeground": "#000000",
            "list.deemphasizedForeground": "#000000",
            "list.dropBackground": "#000000",
            "list.dropBetweenBackground": "#000000",
            "list.errorForeground": "#000000",
            "list.filterMatchBackground": "#000000",
            "list.filterMatchBorder": "#000000",
            "list.focusAndSelectionOutline": "#000000",
            "list.focusBackground": "#000000",
            "list.focusForeground": "#000000",
            "list.focusHighlightForeground": "#000000",
            "list.focusOutline": "#000000",
            "list.highlightForeground": "#000000",
            "list.hoverBackground": "#000000",
            "list.hoverForeground": "#000000",
            "list.inactiveFocusBackground": "#000000",
            "list.inactiveFocusOutline": "#000000",
            "list.inactiveSelectionBackground": "#000000",
            "list.inactiveSelectionForeground": "#000000",
            "list.inactiveSelectionIconForeground": "#000000",
            "list.invalidItemForeground": "#000000",
            "list.warningForeground": "#000000",
            "listFilterWidget.background": "#000000",
            "listFilterWidget.noMatchesOutline": "#000000",
            "listFilterWidget.outline": "#000000",
            "listFilterWidget.shadow": "#000000",
        }

    def menuColors(self):
        return {
            "menu.background": "#000000",
            "menu.border": "#000000",
            "menu.foreground": "#000000",
            "menu.selectionBackground": "#000000",
            "menu.selectionBorder": "#000000",
            "menu.selectionForeground": "#000000",
            "menu.separatorBackground": "#000000",
            "menubar.selectionBackground": "#000000",
            "menubar.selectionBorder": "#000000",
            "menubar.selectionForeground": "#000000",
        }

    def mergeColors(self):
        return {
            "merge.border": "#000000",
            "merge.commonContentBackground": "#000000",
            "merge.commonHeaderBackground": "#000000",
            "merge.currentContentBackground": "#000000",
            "merge.currentHeaderBackground": "#000000",
            "merge.incomingContentBackground": "#000000",
            "merge.incomingHeaderBackground": "#000000",
            "mergeEditor.change.background": "#000000",
            "mergeEditor.change.word.background": "#000000",
            "mergeEditor.changeBase.background": "#000000",
            "mergeEditor.changeBase.word.background": "#000000",
            "mergeEditor.conflict.handled.minimapOverViewRuler": "#000000",
            "mergeEditor.conflict.handledFocused.border": "#000000",
            "mergeEditor.conflict.handledUnfocused.border": "#000000",
            "mergeEditor.conflict.input1.background": "#000000",
            "mergeEditor.conflict.input2.background": "#000000",
            "mergeEditor.conflict.unhandled.minimapOverViewRuler": "#000000",
            "mergeEditor.conflict.unhandledFocused.border": "#000000",
            "mergeEditor.conflict.unhandledUnfocused.border": "#000000",
            "mergeEditor.conflictingLines.background": "#000000",
        }

    def minimapColors(self):
        return {
            "minimap.background": "#000000",
            "minimap.chatEditHighlight": "#000000",
            "minimap.errorHighlight": "#000000",
            "minimap.findMatchHighlight": "#000000",
            "minimap.foregroundOpacity": "#000000",
            "minimap.infoHighlight": "#000000",
            "minimap.selectionHighlight": "#000000",
            "minimap.selectionOccurrenceHighlight": "#000000",
            "minimap.warningHighlight": "#000000",
            "minimapGutter.addedBackground": "#000000",
            "minimapGutter.deletedBackground": "#000000",
            "minimapGutter.modifiedBackground": "#000000",
            "minimapSlider.activeBackground": "#000000",
            "minimapSlider.background": "#000000",
            "minimapSlider.hoverBackground": "#000000",
        }

    def multiDiffEditorColors(self):
        return {
            "multiDiffEditor.background": "#000000",
            "multiDiffEditor.border": "#000000",
            "multiDiffEditor.headerBackground": "#000000",
        }

    def notebookColors(self):
        return {
            "notebook.cellBorderColor": "#000000",
            "notebook.cellEditorBackground": "#000000",
            "notebook.cellHoverBackground": "#000000",
            "notebook.cellInsertionIndicator": "#000000",
            "notebook.cellStatusBarItemHoverBackground": "#000000",
            "notebook.cellToolbarSeparator": "#000000",
            "notebook.editorBackground": "#000000",
            "notebook.focusedCellBackground": "#000000",
            "notebook.focusedCellBorder": "#000000",
            "notebook.focusedEditorBorder": "#000000",
            "notebook.inactiveFocusedCellBorder": "#000000",
            "notebook.inactiveSelectedCellBorder": "#000000",
            "notebook.outputContainerBackgroundColor": "#000000",
            "notebook.outputContainerBorderColor": "#000000",
            "notebook.selectedCellBackground": "#000000",
            "notebook.selectedCellBorder": "#000000",
            "notebook.symbolHighlightBackground": "#000000",
            "notebookEditorOverviewRuler.runningCellForeground": "#000000",
            "notebookScrollbarSlider.activeBackground": "#000000",
            "notebookScrollbarSlider.background": "#000000",
            "notebookScrollbarSlider.hoverBackground": "#000000",
            "notebookStatusErrorIcon.foreground": "#000000",
            "notebookStatusRunningIcon.foreground": "#000000",
            "notebookStatusSuccessIcon.foreground": "#000000",
        }

    def notificationsColors(self):
        return {
            "notificationCenter.border": "#000000",
            "notificationCenterHeader.background": "#000000",
            "notificationCenterHeader.foreground": "#000000",
            "notificationLink.foreground": "#000000",
            "notifications.background": "#000000",
            "notifications.border": "#000000",
            "notifications.foreground": "#000000",
            "notificationsErrorIcon.foreground": "#000000",
            "notificationsInfoIcon.foreground": "#000000",
            "notificationsWarningIcon.foreground": "#000000",
            "notificationToast.border": "#000000",
        }

    def outputViewColors(self):
        return {
            "outputView.background": "#000000",
            "outputViewStickyScroll.background": "#000000",
        }

    def panelColors(self):
        return {
            "panel.background": "#000000",
            "panel.border": "#000000",
            "panel.dropBackground": "#000000",
            "panel.dropBorder": "#000000",
            "panelInput.border": "#000000",
            "panelSection.border": "#000000",
            "panelSection.dropBackground": "#000000",
            "panelSectionHeader.background": "#000000",
            "panelSectionHeader.border": "#000000",
            "panelSectionHeader.foreground": "#000000",
            "panelStickyScroll.background": "#000000",
            "panelStickyScroll.border": "#000000",
            "panelStickyScroll.shadow": "#000000",
            "panelTitle.activeBorder": "#000000",
            "panelTitle.activeForeground": "#000000",
            "panelTitle.border": "#000000",
            "panelTitle.inactiveForeground": "#000000",
            "panelTitleBadge.background": "#000000",
            "panelTitleBadge.foreground": "#000000",
        }

    def peekViewColors(self):
        return {
            "peekView.border": "#000000",
            "peekViewEditor.background": "#000000",
            "peekViewEditor.matchHighlightBackground": "#000000",
            "peekViewEditor.matchHighlightBorder": "#000000",
            "peekViewEditorGutter.background": "#000000",
            "peekViewEditorStickyScroll.background": "#000000",
            "peekViewResult.background": "#000000",
            "peekViewResult.fileForeground": "#000000",
            "peekViewResult.lineForeground": "#000000",
            "peekViewResult.matchHighlightBackground": "#000000",
            "peekViewResult.selectionBackground": "#000000",
            "peekViewResult.selectionForeground": "#000000",
            "peekViewTitle.background": "#000000",
            "peekViewTitleDescription.foreground": "#000000",
            "peekViewTitleLabel.foreground": "#000000",
        }

    def pickerGroupColors(self):
        return {
            "pickerGroup.border": "#000000",
            "pickerGroup.foreground": "#000000",
        }

    def portsColors(self):
        return {
            "ports.iconRunningProcessForeground": "#000000",
        }

    def problemsColors(self):
        return {
            "problemsErrorIcon.foreground": "#000000",
            "problemsInfoIcon.foreground": "#000000",
            "problemsWarningIcon.foreground": "#000000",
        }

    def profileColors(self):
        return {
            "profileBadge.background": "#000000",
            "profileBadge.foreground": "#000000",
            "profiles.sashBorder": "#000000",
        }

    def progressBarColors(self):
        return {
            "progressBar.background": "#000000",
        }

    def pullRequestsColors(self):
        return {
            "pullRequests.draft": "#000000",
            "pullRequests.merged": "#000000",
            "pullRequests.notification": "#000000",
            "pullRequests.open": "#000000",
        }

    def quickInputColors(self):
        return {
            "quickInput.background": "#000000",
            "quickInput.foreground": "#000000",
            "quickInputList.focusBackground": "#000000",
            "quickInputList.focusForeground": "#000000",
            "quickInputList.focusIconForeground": "#000000",
            "quickInputTitle.background": "#000000",
        }

    def radioColors(self):
        return {
            "radio.activeBackground": "#000000",
            "radio.activeBorder": "#000000",
            "radio.activeForeground": "#000000",
            "radio.inactiveBackground": "#000000",
            "radio.inactiveBorder": "#000000",
            "radio.inactiveForeground": "#000000",
            "radio.inactiveHoverBackground": "#000000",
        }

    def sashColors(self):
        return {
            "sash.hoverBorder": "#000000",
        }

    def scmGraphColors(self):
        return {
            "scmGraph.foreground1": "#000000",
            "scmGraph.foreground2": "#000000",
            "scmGraph.foreground3": "#000000",
            "scmGraph.foreground4": "#000000",
            "scmGraph.foreground5": "#000000",
            "scmGraph.historyItemBaseRefColor": "#000000",
            "scmGraph.historyItemHoverAdditionsForeground": "#000000",
            "scmGraph.historyItemHoverDefaultLabelBackground": "#000000",
            "scmGraph.historyItemHoverDefaultLabelForeground": "#000000",
            "scmGraph.historyItemHoverDeletionsForeground": "#000000",
            "scmGraph.historyItemHoverLabelForeground": "#000000",
            "scmGraph.historyItemRefColor": "#000000",
            "scmGraph.historyItemRemoteRefColor": "#000000",
        }

    def scrollBarColors(self):
        return {
            "scrollbar.shadow": "#000000",
            "scrollbarSlider.activeBackground": "#000000",
            "scrollbarSlider.background": "#000000",
            "scrollbarSlider.hoverBackground": "#000000",
        }

    def searchColors(self):
        return {
            "search.resultsInfoForeground": "#000000",
            "searchEditor.findMatchBackground": "#000000",
            "searchEditor.findMatchBorder": "#000000",
            "searchEditor.textInputBorder": "#000000",
        }

    def selectionColors(self):
        return {
            "selection.background": "#000000",
        }

    def settingsColors(self):
        return {
            "settings.checkboxBackground": "#000000",
            "settings.checkboxBorder": "#000000",
            "settings.checkboxForeground": "#000000",
            "settings.dropdownBackground": "#000000",
            "settings.dropdownBorder": "#000000",
            "settings.dropdownForeground": "#000000",
            "settings.dropdownListBorder": "#000000",
            "settings.focusedRowBackground": "#000000",
            "settings.focusedRowBorder": "#000000",
            "settings.headerBorder": "#000000",
            "settings.headerForeground": "#000000",
            "settings.modifiedItemIndicator": "#000000",
            "settings.numberInputBackground": "#000000",
            "settings.numberInputBorder": "#000000",
            "settings.numberInputForeground": "#000000",
            "settings.rowHoverBackground": "#000000",
            "settings.sashBorder": "#000000",
            "settings.settingsHeaderHoverForeground": "#000000",
            "settings.textInputBackground": "#000000",
            "settings.textInputBorder": "#000000",
            "settings.textInputForeground": "#000000",
        }

    def sideBarColors(self):
        return {
            "sideBar.background": "#000000",
            "sideBar.border": "#000000",
            "sideBar.dropBackground": "#000000",
            "sideBar.foreground": "#000000",
            "sideBarActivityBarTop.border": "#000000",
            "sideBarSectionHeader.background": "#000000",
            "sideBarSectionHeader.border": "#000000",
            "sideBarSectionHeader.foreground": "#000000",
            "sideBarStickyScroll.background": "#000000",
            "sideBarStickyScroll.border": "#000000",
            "sideBarStickyScroll.shadow": "#000000",
            "sideBarTitle.background": "#000000",
            "sideBarTitle.border": "#000000",
            "sideBarTitle.foreground": "#000000",
            "sideBySideEditor.horizontalBorder": "#000000",
            "sideBySideEditor.verticalBorder": "#000000",
            "simpleFindWidget.sashBorder": "#000000",
        }

    def statusBarColors(self):
        return {
            "statusBar.background": "#000000",
            "statusBar.border": "#000000",
            "statusBar.debuggingBackground": "#000000",
            "statusBar.debuggingBorder": "#000000",
            "statusBar.debuggingForeground": "#000000",
            "statusBar.focusBorder": "#000000",
            "statusBar.foreground": "#000000",
            "statusBar.noFolderBackground": "#000000",
            "statusBar.noFolderBorder": "#000000",
            "statusBar.noFolderForeground": "#000000",
            "statusBarItem.activeBackground": "#000000",
            "statusBarItem.compactHoverBackground": "#000000",
            "statusBarItem.errorBackground": "#000000",
            "statusBarItem.errorForeground": "#000000",
            "statusBarItem.errorHoverBackground": "#000000",
            "statusBarItem.errorHoverForeground": "#000000",
            "statusBarItem.focusBorder": "#000000",
            "statusBarItem.hoverBackground": "#000000",
            "statusBarItem.hoverForeground": "#000000",
            "statusBarItem.offlineBackground": "#000000",
            "statusBarItem.offlineForeground": "#000000",
            "statusBarItem.offlineHoverBackground": "#000000",
            "statusBarItem.offlineHoverForeground": "#000000",
            "statusBarItem.prominentBackground": "#000000",
            "statusBarItem.prominentForeground": "#000000",
            "statusBarItem.prominentHoverBackground": "#000000",
            "statusBarItem.prominentHoverForeground": "#000000",
            "statusBarItem.remoteBackground": "#000000",
            "statusBarItem.remoteForeground": "#000000",
            "statusBarItem.remoteHoverBackground": "#000000",
            "statusBarItem.remoteHoverForeground": "#000000",
            "statusBarItem.warningBackground": "#000000",
            "statusBarItem.warningForeground": "#000000",
            "statusBarItem.warningHoverBackground": "#000000",
            "statusBarItem.warningHoverForeground": "#000000",
        }

    def symbolIconsColors(self):
        return {
            "symbolIcon.arrayForeground": "#000000",
            "symbolIcon.booleanForeground": "#000000",
            "symbolIcon.classForeground": "#000000",
            "symbolIcon.colorForeground": "#000000",
            "symbolIcon.constantForeground": "#000000",
            "symbolIcon.constructorForeground": "#000000",
            "symbolIcon.enumeratorForeground": "#000000",
            "symbolIcon.enumeratorMemberForeground": "#000000",
            "symbolIcon.eventForeground": "#000000",
            "symbolIcon.fieldForeground": "#000000",
            "symbolIcon.fileForeground": "#000000",
            "symbolIcon.folderForeground": "#000000",
            "symbolIcon.functionForeground": "#000000",
            "symbolIcon.interfaceForeground": "#000000",
            "symbolIcon.keyForeground": "#000000",
            "symbolIcon.keywordForeground": "#000000",
            "symbolIcon.methodForeground": "#000000",
            "symbolIcon.moduleForeground": "#000000",
            "symbolIcon.namespaceForeground": "#000000",
            "symbolIcon.nullForeground": "#000000",
            "symbolIcon.numberForeground": "#000000",
            "symbolIcon.objectForeground": "#000000",
            "symbolIcon.operatorForeground": "#000000",
            "symbolIcon.packageForeground": "#000000",
            "symbolIcon.propertyForeground": "#000000",
            "symbolIcon.referenceForeground": "#000000",
            "symbolIcon.snippetForeground": "#000000",
            "symbolIcon.stringForeground": "#000000",
            "symbolIcon.structForeground": "#000000",
            "symbolIcon.textForeground": "#000000",
            "symbolIcon.typeParameterForeground": "#000000",
            "symbolIcon.unitForeground": "#000000",
            "symbolIcon.variableForeground": "#000000",
        }

    def tabColors(self):
        return {
            "tab.activeBackground": "#000000",
            "tab.activeBorder": "#000000",
            "tab.activeBorderTop": "#000000",
            "tab.activeForeground": "#000000",
            "tab.activeModifiedBorder": "#000000",
            "tab.border": "#000000",
            "tab.dragAndDropBorder": "#000000",
            "tab.hoverBackground": "#000000",
            "tab.hoverBorder": "#000000",
            "tab.hoverForeground": "#000000",
            "tab.inactiveBackground": "#000000",
            "tab.inactiveForeground": "#000000",
            "tab.inactiveModifiedBorder": "#000000",
            "tab.lastPinnedBorder": "#000000",
            "tab.selectedBackground": "#000000",
            "tab.selectedBorderTop": "#000000",
            "tab.selectedForeground": "#000000",
            "tab.unfocusedActiveBackground": "#000000",
            "tab.unfocusedActiveBorder": "#000000",
            "tab.unfocusedActiveBorderTop": "#000000",
            "tab.unfocusedActiveForeground": "#000000",
            "tab.unfocusedActiveModifiedBorder": "#000000",
            "tab.unfocusedHoverBackground": "#000000",
            "tab.unfocusedHoverBorder": "#000000",
            "tab.unfocusedHoverForeground": "#000000",
            "tab.unfocusedInactiveForeground": "#000000",
            "tab.unfocusedInactiveModifiedBorder": "#000000",
        }

    def terminalColors(self):
        return {
            "terminal.ansiBlack": "#000000",
            "terminal.ansiBlue": "#000000",
            "terminal.ansiBrightBlack": "#000000",
            "terminal.ansiBrightBlue": "#000000",
            "terminal.ansiBrightCyan": "#000000",
            "terminal.ansiBrightGreen": "#000000",
            "terminal.ansiBrightMagenta": "#000000",
            "terminal.ansiBrightRed": "#000000",
            "terminal.ansiBrightWhite": "#000000",
            "terminal.ansiBrightYellow": "#000000",
            "terminal.ansiCyan": "#000000",
            "terminal.ansiGreen": "#000000",
            "terminal.ansiMagenta": "#000000",
            "terminal.ansiRed": "#000000",
            "terminal.ansiWhite": "#000000",
            "terminal.ansiYellow": "#000000",
            "terminal.background": "#000000",
            "terminal.border": "#000000",
            "terminal.dropBackground": "#000000",
            "terminal.findMatchBackground": "#000000",
            "terminal.findMatchBorder": "#000000",
            "terminal.findMatchHighlightBackground": "#000000",
            "terminal.findMatchHighlightBorder": "#000000",
            "terminal.foreground": "#000000",
            "terminal.hoverHighlightBackground": "#000000",
            "terminal.inactiveSelectionBackground": "#000000",
            "terminal.initialHintForeground": "#000000",
            "terminal.selectionBackground": "#000000",
            "terminal.selectionForeground": "#000000",
            "terminal.tab.activeBorder": "#000000",
            "terminalCommandDecoration.defaultBackground": "#000000",
            "terminalCommandDecoration.errorBackground": "#000000",
            "terminalCommandDecoration.successBackground": "#000000",
            "terminalCommandGuide.foreground": "#000000",
            "terminalCursor.background": "#000000",
            "terminalCursor.foreground": "#000000",
            "terminalOverviewRuler.border": "#000000",
            "terminalOverviewRuler.cursorForeground": "#000000",
            "terminalOverviewRuler.findMatchForeground": "#000000",
            "terminalStickyScroll.background": "#000000",
            "terminalStickyScroll.border": "#000000",
            "terminalStickyScrollHover.background": "#000000",
            "terminalSymbolIcon.aliasForeground": "#000000",
            "terminalSymbolIcon.argumentForeground": "#000000",
            "terminalSymbolIcon.fileForeground": "#000000",
            "terminalSymbolIcon.flagForeground": "#000000",
            "terminalSymbolIcon.folderForeground": "#000000",
            "terminalSymbolIcon.inlineSuggestionForeground": "#000000",
            "terminalSymbolIcon.methodForeground": "#000000",
            "terminalSymbolIcon.optionForeground": "#000000",
            "terminalSymbolIcon.optionValueForeground": "#000000",
        }

    def testingColors(self):
        return {
            "testing.coverCountBadgeBackground": "#000000",
            "testing.coverCountBadgeForeground": "#000000",
            "testing.coveredBackground": "#000000",
            "testing.coveredBorder": "#000000",
            "testing.coveredGutterBackground": "#000000",
            "testing.iconErrored": "#000000",
            "testing.iconErrored.retired": "#000000",
            "testing.iconFailed": "#000000",
            "testing.iconFailed.retired": "#000000",
            "testing.iconPassed": "#000000",
            "testing.iconPassed.retired": "#000000",
            "testing.iconQueued": "#000000",
            "testing.iconQueued.retired": "#000000",
            "testing.iconSkipped": "#000000",
            "testing.iconSkipped.retired": "#000000",
            "testing.iconUnset": "#000000",
            "testing.iconUnset.retired": "#000000",
            "testing.message.error.badgeBackground": "#000000",
            "testing.message.error.badgeBorder": "#000000",
            "testing.message.error.badgeForeground": "#000000",
            "testing.message.error.lineBackground": "#000000",
            "testing.message.info.decorationForeground": "#000000",
            "testing.message.info.lineBackground": "#000000",
            "testing.messagePeekBorder": "#000000",
            "testing.messagePeekHeaderBackground": "#000000",
            "testing.peekBorder": "#000000",
            "testing.peekHeaderBackground": "#000000",
            "testing.runAction": "#000000",
            "testing.uncoveredBackground": "#000000",
            "testing.uncoveredBorder": "#000000",
            "testing.uncoveredBranchBackground": "#000000",
            "testing.uncoveredGutterBackground": "#000000",
        }

    def textColors(self):
        return {
            "textBlockQuote.background": "#000000",
            "textBlockQuote.border": "#000000",
            "textCodeBlock.background": "#000000",
            "textLink.activeForeground": "#000000",
            "textLink.foreground": "#000000",
            "textPreformat.background": "#000000",
            "textPreformat.foreground": "#000000",
            "textSeparator.foreground": "#000000",
        }

    def titleBarColors(self):
        return {
            "titleBar.activeBackground": "#000000",
            "titleBar.activeForeground": "#000000",
            "titleBar.border": "#000000",
            "titleBar.inactiveBackground": "#000000",
            "titleBar.inactiveForeground": "#000000",
        }

    def toolbarColors(self):
        return {
            "toolbar.activeBackground": "#000000",
            "toolbar.hoverBackground": "#000000",
            "toolbar.hoverOutline": "#000000",
        }

    def treeColors(self):
        return {
            "tree.inactiveIndentGuidesStroke": "#000000",
            "tree.indentGuidesStroke": "#000000",
            "tree.tableColumnsBorder": "#000000",
            "tree.tableOddRowsBackground": "#000000",
        }

    def walkThroughColors(self):
        return {
            "walkThrough.embeddedEditorBackground": "#000000",
            "walkthrough.stepTitle.foreground": "#000000",
        }

    def welcomePageColors(self):
        return {
            "welcomePage.background": "#000000",
            "welcomePage.progress.background": "#000000",
            "welcomePage.progress.foreground": "#000000",
            "welcomePage.tileBackground": "#000000",
            "welcomePage.tileBorder": "#000000",
            "welcomePage.tileHoverBackground": "#000000",
        }

    def widgetColors(self):
        return {
            "widget.border": "#000000",
            "widget.shadow": "#000000",
        }

    def windowColors(self):
        return {"window.activeBorder": "#000000", "window.inactiveBorder": "#000000"}
